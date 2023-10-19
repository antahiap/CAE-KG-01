from django.shortcuts import render
from django.views import generic
from kg01_model.models import (
    Sim
)

import json

class ClusterOrder(generic.TemplateView):

    template_name = 'energy_cluster/cluster_pid_order_plot.html'

    def get_context_data(self, **kwargs):

        run_name = self.kwargs.get('run_name')
        # model_name = self.kwargs.get('model_name')
        # oem = self.kwargs.get('oem')

        run_name_list = run_name.split(',')
        # model_name_list = model_name.split(',')

        runs = run_name_list

        y,runName,yZip = [],[],[]
        for ri in runs:
            print(ri)
            runName.append(ri)
            sim = Sim.nodes.get(sim_name = ri)

            yr = sim.get_part()
            for yi in yr:
                if yi not in yZip:
                    yZip.append(yi)
            y.append([yZip.index(yi) for yi in yr])
        print(yr)
        context = super().get_context_data(**kwargs)
        context['x'] = range(1, len(y[0])+1)
        context['y'] = y
        context['ystr'] = [str(i) for i in yZip]
        context['yZip'] = yZip
        # context['run_list'] = json.dumps(run_name_list)
        context['run_list'] = runName
        return context
