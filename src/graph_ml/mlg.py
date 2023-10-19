from torch_geometric.datasets import KarateClub
# import matplotlib.pyplot as plt
import networkx as nx
import os
import torch
# from IPython.display import display
# from IPython.display import Javascript  # Restrict height of output cell.
import torch
from torch.nn import Linear
from torch_geometric.nn import GCNConv
import time
import pandas as pd
import torch.nn.functional as F
import torch_geometric.transforms as T
from torch_geometric.loader import DataLoader
from ogb.nodeproppred import PygNodePropPredDataset, Evaluator
import copy
from tqdm import tqdm

# Helper function for visualization.
# %matplotlib inline

# Visualization function for NX graph or PyTorch tensor


def visualize(h, color, epoch=None, loss=None):
    plt.figure(figsize=(7, 7))
    plt.xticks([])
    plt.yticks([])

    if torch.is_tensor(h):
        h = h.detach().cpu().numpy()
        plt.scatter(h[:, 0], h[:, 1], s=140, c=color, cmap="Set2")
        if epoch is not None and loss is not None:
            plt.xlabel(f'Epoch: {epoch}, Loss: {loss.item():.4f}', fontsize=16)
    else:
        nx.draw_networkx(h, pos=nx.spring_layout(h, seed=42), with_labels=False,
                         node_color=color, cmap="Set2")
    plt.show()


def colab0():

    print("PyTorch has version {}".format(torch.__version__))
    # General
    dataset = KarateClub()
    print(f'Dataset: {dataset}:')
    print('======================')
    print(f'Number of graphs: {len(dataset)}')
    print(f'Number of features: {dataset.num_features}')
    print(f'Number of classes: {dataset.num_classes}')

    data = dataset[0]  # Get the first graph object.

    print(data)
    print('==============================================================')

    # Gather some statistics about the graph.
    print(f'Number of nodes: {data.num_nodes}')
    print(f'Number of edges: {data.num_edges}')
    print(f'Average node degree: {data.num_edges / data.num_nodes:.2f}')
    print(f'Number of training nodes: {data.train_mask.sum()}')
    print(
        f'Training node label rate: {int(data.train_mask.sum()) / data.num_nodes:.2f}')
    print(f'Contains isolated nodes: {data.contains_isolated_nodes()}')
    print(f'Contains self-loops: {data.contains_self_loops()}')
    print(f'Is undirected: {data.is_undirected()}')

    from IPython.display import Javascript  # Restrict height of output cell.
    display(Javascript(
        '''google.colab.output.setIframeHeight(0, true, {maxHeight: 300})'''))

    edge_index = data.edge_index
    print(edge_index.t())

    from torch_geometric.utils import to_networkx
    G = to_networkx(data, to_undirected=True)
    # visualize(G, color=data.y)

    class GCN(torch.nn.Module):
        def __init__(self):
            super(GCN, self).__init__()
            torch.manual_seed(12345)
            self.conv1 = GCNConv(dataset.num_features, 4)
            self.conv2 = GCNConv(4, 4)
            self.conv3 = GCNConv(4, 2)
            self.classifier = Linear(2, dataset.num_classes)

        def forward(self, x, edge_index):
            h = self.conv1(x, edge_index)
            h = h.tanh()
            h = self.conv2(h, edge_index)
            h = h.tanh()
            h = self.conv3(h, edge_index)
            h = h.tanh()  # Final GNN embedding space.

            # Apply a final (linear) classifier.
            out = self.classifier(h)

            return out, h

    model = GCN()
    print(model)

    _, h = model(data.x, data.edge_index)
    print(f'Embedding shape: {list(h.shape)}')
    # visualize(h, color=data.y)

    display(Javascript(
        '''google.colab.output.setIframeHeight(0, true, {maxHeight: 430})'''))

    model = GCN()
    criterion = torch.nn.CrossEntropyLoss()  # Define loss criterion.
    # Define optimizer.
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    def train(data):
        optimizer.zero_grad()  # Clear gradients.
        # Perform a single forward pass.
        out, h = model(data.x, data.edge_index)
        # Compute the loss solely based on the training nodes.
        loss = criterion(out[data.train_mask], data.y[data.train_mask])
        loss.backward()  # Derive gradients.
        optimizer.step()  # Update parameters based on gradients.
        return loss, h

    for epoch in range(401):
        loss, h = train(data)
        # Visualize the node embeddings every 10 epochs
        if epoch % 10 == 0:
            visualize(h, color=data.y, epoch=epoch, loss=loss)
            time.sleep(0.3)


def colab0_err():

    class BuggyGCN(torch.nn.Module):
        def __init__(self, args, dataset):
            super(BuggyGCN, self).__init__()
            torch.manual_seed(12345)

            self.conv = Sequential(
                GCNConv(dataset.num_features, args["hidden_size"]),
                Tanh(),
                GCNConv(args["hidden_size"], args["hidden_size"]),
                Tanh(),
                GCNConv(args["hidden_size"], args["hidden_size"])
            )

            self.classifier = Linear(2, dataset.num_classes)

        def forward(self, x, edge_index):
            h = self.conv(x, edge_index)  # GNN embedding space.

            # Apply a final (linear) classifier.
            out = self.classifier(h)

            return out, h

    # Feel free to change the following parameters
    args = {
        'device': torch.device('cuda' if torch.cuda.is_available() else 'cpu'),
        'hidden_size': 4,
        'epochs': 401,
        'lr': 0.01,
        'sleep': 0.2
    }

    model = BuggyGCN(args, dataset)
    criterion = torch.nn.CrossEntropyLoss()  # Define loss criterion.
    # Define optimizer.
    optimizer = torch.optim.Adam(model.parameters(), lr=args["lr"])

    with tqdm(range(args["epochs"]), unit="batch") as tepoch:
        for epoch in tepoch:
            loss, h = train(data)
            tepoch.set_description(f'Epoch {epoch} - Loss {loss.item()}')
            time.sleep(args['sleep'])


def colab1():
    G = nx.karate_club_graph()

    # G is an undirected graph
    type(G)

    # Visualize the graph
    # if 'IS_GRADESCOPE_ENV' not in os.environ:
    # nx.draw(G, with_labels=True)
    # plt.show()


def colab2():
    GCN_npp()
    # GNN_gpp()

def GNN_gpp():

  # Load the dataset 
  dataset = PygGraphPropPredDataset(name='ogbg-molhiv')

  device = 'cuda' if torch.cuda.is_available() else 'cpu'
  print('Device: {}'.format(device))

  split_idx = dataset.get_idx_split()

  # Check task type
  print('Task type: {}'.format(dataset.task_type))

def GCN_npp():
    '''
    
    # 3) GNN: Node Property Prediction
    
    In this section you will build your first graph neural network using PyTorch Geometric. Then you will apply it to the task of node property prediction (node classification).
        
    Specifically, you will use GCN as the foundation for your graph neural network ([Kipf et al. (2017)](https://arxiv.org/pdf/1609.02907.pdf)). To do so, you will work with PyG's built-in `GCNConv` layer. 
    '''

    class GCN(torch.nn.Module):
        def __init__(self, input_dim, hidden_dim, output_dim, num_layers,
                     dropout, return_embeds=False):
            # TODO: Implement the init function that initializes self.convs,
            # self.bns, and self.softmax.

            super(GCN, self).__init__()

            # A list of GCNConv layers
            self.convs = None

            # A list of 1D batch normalization layers
            self.bns = None

            # The log softmax layer
            self.softmax = None

            ############# Your code here ############
            # Note:
            # 1. Use torch.nn.ModuleList for self.convs and self.bns
            # 2. self.convs has num_layers GCNConv layers
            # 3. self.bns has num_layers - 1 BatchNorm1d layers
            # 4. Use torch.nn.LogSoftmax for self.softmax
            # 5. The GCNConv layer takes as input 'in_channels' and
            # 'out_channels'. For more information please refer to the documentation:
            # https://pytorch-geometric.readthedocs.io/en/latest/modules/nn.html#torch_geometric.nn.conv.GCNConv
            # 6. The only parameter BatchNorm1d requires is 'num_features'
            # For more information please refer to the documentation:
            # https://pytorch.org/docs/stable/generated/torch.nn.BatchNorm1d.html
            # (~10 lines of code)
            self.convs = torch.nn.ModuleList(
                [GCNConv(in_channels=input_dim, out_channels=hidden_dim)] +
                [GCNConv(in_channels=hidden_dim, out_channels=hidden_dim)
                    for i in range(num_layers-2)] +
                [GCNConv(in_channels=hidden_dim, out_channels=output_dim)])
            self.bns = torch.nn.ModuleList(
                [torch.nn.BatchNorm1d(num_features=hidden_dim)
                    for i in range(num_layers-1)])
            self.softmax = torch.nn.LogSoftmax()
            pass
            #########################################

            # Probability of an element getting zeroed
            self.dropout = dropout

            # Skip classification layer and return node embeddings
            self.return_embeds = return_embeds

        def reset_parameters(self):
            for conv in self.convs:
                conv.reset_parameters()
            for bn in self.bns:
                bn.reset_parameters()

        def forward(self, x, adj_t):
            # TODO: Implement a function that takes as input a feature tensor x
            # and edge_index tensor adj_t, and returns the corresponding output
            # tensor as shown in the figure above.

            out = None

            ############# Your code here ############
            # Note:
            # 1. Construct the network as shown in the figure
            # 2. torch.nn.functional.relu and torch.nn.functional.dropout are useful
            # For more information please refer to the documentation:
            # https://pytorch.org/docs/stable/nn.functional.html
            # 3. Don't forget to set F.dropout training to self.training
            # 4. If return_embeds is True, then skip the last softmax layer
            # (~7 lines of code)
            for conv, bn in zip(self.convs[:-1], self.bns):
                x1 = F.relu(bn(conv(x, adj_t)))
                if self.training:
                    x1 = F.dropout(x1, p=self.dropout)
                x = x1
            x = self.convs[-1](x, adj_t)
            out = x if self.return_embeds else self.softmax(x)
            pass
            #########################################

            return out

    def train(model, data, train_idx, optimizer, loss_fn):
        # TODO: Implement a function that trains the model by
        # using the given optimizer and loss_fn.
        model.train()
        loss = 0

        ############# Your code here ############
        # Note:
        # 1. Zero grad the optimizer
        # 2. Feed the data into the model
        # 3. Slice the model outputs and labels by train_idx
        # 4. Feed the sliced outputs and labels to the loss_fn
        # (~4 lines of code)
        optimizer.zero_grad()
        out = model(data.x, data.adj_t)
        loss = loss_fn(out[train_idx], data.y[train_idx].reshape(-1))
        pass
        #########################################

        loss.backward()
        optimizer.step()

        return loss.item()

    # Test function here
    @torch.no_grad()
    def test(model, data, split_idx, evaluator, save_model_results=False):
        # TODO: Implement a function that tests the model by
        # using the given split_idx and ogb evaluator.
        model.eval()

        # The output of model on all data
        out = None

        ############# Your code here ############
        # (~1 line of code)
        # Note:
        # 1. No index slicing here
        out = model(data.x, data.adj_t)
        pass
        #########################################

        y_pred = out.argmax(dim=-1, keepdim=True)

        train_acc = evaluator.eval({
            'y_true': data.y[split_idx['train']],
            'y_pred': y_pred[split_idx['train']],
        })['acc']
        valid_acc = evaluator.eval({
            'y_true': data.y[split_idx['valid']],
            'y_pred': y_pred[split_idx['valid']],
        })['acc']
        test_acc = evaluator.eval({
            'y_true': data.y[split_idx['test']],
            'y_pred': y_pred[split_idx['test']],
        })['acc']

        if save_model_results:
            print("Saving Model Predictions")

            data = {}
            data['y_pred'] = y_pred.view(-1).cpu().detach().numpy()

            df = pd.DataFrame(data=data)
            # Save locally as csv
            df.to_csv('ogbn-arxiv_node.csv', sep=',', index=False)

        return train_acc, valid_acc, test_acc

    dataset_name = 'ogbn-arxiv'
    dataset = PygNodePropPredDataset(name=dataset_name,
                                     transform=T.ToSparseTensor())
    data = dataset[0]

    # Make the adjacency matrix to symmetric
    data.adj_t = data.adj_t.to_symmetric()

    device = 'cuda' if torch.cuda.is_available() else 'cpu'

    # If you use GPU, the device should be cuda
    print('Device: {}'.format(device))

    data = data.to(device)
    split_idx = dataset.get_idx_split()
    train_idx = split_idx['train'].to(device)

    # Please do not change the args
    args = {
        'device': device,
        'num_layers': 3,
        'hidden_dim': 256,
        'dropout': 0.5,
        'lr': 0.01,
        'epochs': 100,
    }
    args

    model = GCN(data.num_features, args['hidden_dim'],
                dataset.num_classes, args['num_layers'],
                args['dropout']).to(device)
    evaluator = Evaluator(name='ogbn-arxiv')

    # reset the parameters to initial random value
    model.reset_parameters()

    optimizer = torch.optim.Adam(model.parameters(), lr=args['lr'])
    loss_fn = F.nll_loss

    best_model = None
    best_valid_acc = 0

    for epoch in range(1, 1 + args["epochs"]):
        loss = train(model, data, train_idx, optimizer, loss_fn)
        result = test(model, data, split_idx, evaluator)
        train_acc, valid_acc, test_acc = result
        if valid_acc > best_valid_acc:
            best_valid_acc = valid_acc
            best_model = copy.deepcopy(model)
        print(f'Epoch: {epoch:02d}, '
              f'Loss: {loss:.4f}, '
              f'Train: {100 * train_acc:.2f}%, '
              f'Valid: {100 * valid_acc:.2f}% '
              f'Test: {100 * test_acc:.2f}%')


if __name__ == '__main__':
    # colab0()
    # colab0_err()

    # colab1()
    colab2()
