
import dash
import sys
import os
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output 
from dash.exceptions import PreventUpdate
import plotly.express as px

sys.path.append(os.path.abspath('..'))
sys.path.append(os.path.abspath('../note_scripts/'))
# import cypher_notebook_nrg as cyNrg
import oems

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}
def set_plots(c_grp, ords, ns, nPid, sims, pids):
    oem = oems.oems('CEVT')
    # df1 = oem.cypher().out_power_law_df('.*m1_.*')
    df1 = oem.cypher().out_dataframe(
        ns=int(ns), nPID=int(nPid), nOrd=ords, regs=sims, regp=pids)

    df1 = df1.drop_duplicates('PID', keep='first')
    df1 = df1.sort_values(by=['count'], ascending=False)

    df_top = df1[df1['count'] > 1]
    df_top['PID'] = df_top['PID'].astype(str)

    h_data = {
        "sim": True,
        "c_grPID": False,
        "IE": ':.2f',
        "ti": ':.3f',
        "tn": ':.2f'}
    fig1 = px.bar(df_top, x='PID', y='count',
                    #color=c_grp, 
                    custom_data=["pic"],
                    hover_name="PID",
                    hover_data=h_data)
    # df1 = oem.cypher().out_dataframe(
    #     ns=int(ns), nPID=int(nPid), nOrd=ords, regs=sims, regp=pids)

    # fig1 = px.scatter_3d(
        # df1, x="tn", y="ti", z="IE", color=c_grp, custom_data=["pic"],
        # hover_name="PID",
        # hover_data=h_data)
    fig1.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig1.update_layout(showlegend=False, height=700)


    return fig1

c_grp='c_grPID'
c_grp='c_grOrd'
ords=3
ns=2
nPid=1
sims='.*_m1.*fo5.*'
pids=''
fig1 = set_plots(c_grp, ords, ns, nPid, sims, pids)




app.layout = html.Div([
    html.Div(className='row', children=[
        html.Div(
            dcc.Graph(id='power-law', figure=fig1),
            className='six columns'),
        html.Div(
            className='three columns',
            children=[
                html.Pre(id='click-data'),
                html.Pre(id='click-data2')
                ]
        ),
        ]),
    html.Div(
        className='row',
        children=[
            html.Div(
                className='nine columns',
                children=[
                    html.Div(
                        children=[
                        html.Div(className='four columns', children=[
                            dcc.Input(
                                placeholder='Enter sims list or regex...',
                                type='text',
                                value=sims,
                                id='sims'),
                            dcc.Input(
                                placeholder='Enter pids list or regex...',
                                type='text',
                                value='',
                                id='pids'),
                            dcc.Input(
                                placeholder='Max No Ord...',
                                type='number',
                                value=ords,
                                id='ords'),
                            dcc.Input(
                                placeholder='Max No sim...',
                                type='number',
                                value=ns,
                                id='ns'),
                            dcc.Input(
                                placeholder='Max No PIDs',
                                type='number',
                                value=nPid,
                                id='nPid')
                            ], style={'columnCount': 2}),
                        html.Div(dcc.Dropdown(
                            options=[
                                {'label': 'Sim Group', 'value': 'c_grSim'},
                                {'label': 'PID Group', 'value': 'c_grPID'},
                                {'label': 'Ord Group', 'value': 'c_grOrd'},
                                {'label': 'Release Group', 'value': 'c_rls'},
                                {'label': 'Loadcase Group', 'value': 'c_lc'}],
                            value=c_grp, id='c_grp'),
                            className='two columns'),
                        html.Div(children=[dcc.Dropdown(
                            options=[
                                {'label': 'Top', 'value': 'top'},
                                {'label': 'Iso', 'value': 'iso'},
                                {'label': 'Single', 'value': 'iso0'},
                                {'label': 'vTop', 'value': 'top.mp4'},
                                {'label': 'vBtm', 'value': 'btm.mp4'},
                                {'label': 'vFront', 'value': 'front.mp4'},
                                {'label': 'vRight', 'value': 'right.mp4'},
                                ],
                            value='iso', id='pic_view'),
                            html.Button('Submit', id='update'),
                            html.Button('Reset', id = 'reset')],
                            className='two columns'),
                        html.Div(
                            className='three columns',
                            children=[
                                html.Pre(id='click-data-txt'),#, style=styles['pre'])]
                                html.Pre(id='click-data-txt2')]#, style=styles['pre'])]
                        ),
            ])]),
            html.Div(
                className='three columns',
                children=[
                    dcc.Slider(id='time', min=0, max=13, value=7),
                    html.Pre(id='sTime')
                ]
            )
            ])

    ])


@app.callback(
    [Output('power-law', 'figure'),
    ],
    [
        Input('c_grp', 'value'),
        Input('ords', 'value'),
        Input('nPid', 'value'),
        Input('ns', 'value'),
        Input('sims', 'value'),
        Input('pids', 'value'),
        Input('update', component_property='n_clicks'),
    ]
        )
def update_embd_3d(c_grp, ords, nPid, ns, sims, pids, n_clicks):
    if n_clicks is None:
        raise PreventUpdate
    else:
        return [set_plots(c_grp, ords, ns, nPid, sims, pids)]


@app.callback(
    [
        Output('click-data', 'children'),
        Output('click-data-txt', 'children'),
        Output('click-data-txt2', 'children'),
        Output('sTime', 'children'),
        Output('power-law', 'clickData'),
        Output('reset', component_property='n_clicks'),
    ],
    [
        Input('power-law', 'clickData'),
        Input('pic_view', 'value'),
        Input('click-data-txt2', 'children'),
        Input('time', 'value'),
        Input('sTime', 'children'),
        Input('reset', component_property='n_clicks'),
    ])
def display_click_data(cData1, 
    pos, old, tVal, sTime, reset):
    c_i = None
    
    pids,sims = [], []

    txt = 'sims: {0}\npids: {1}'.format(
            ', '.join(sims),
            ', '.join(pids)
        )
    
    if old:
        sims, pids = old.split('\n')
    else:
        sims, pids = ' ', ' '
    if cData1:
        pid_i = cData1['points'][0]['hovertext']
        sim_i = cData1['points'][0]['customdata'][1]
        c_i = cData1['points'][0]['customdata'][0]
        if not sim_i in sims:
            sims += ( sim_i + ', ')
        if not pid_i in pids:
            pids += ( pid_i + ', ')



    txt2 = '{0}\n{1}'.format(sims,pids)
    if not reset is None:
        txt2 = ''
        txt = 'sims: \npids:'

    if sTime and not c_i:
        try:
            sim_i = sTime.split('/')[2]
            sim_i = '_'.join(sim_i.split('_')[:-2])
        except IndexError:
            sTime_1 = sTime.split('/')[1]
            sim_i = '_'.join(sTime_1.split('_')[:-2])
            pass
        # c_i = '_'.join(sTime.split('_')[:-1] + ['POS.png'])
    if c_i:
        if 'mp4' in pos:
            extn = '_{}.png'.format(tVal)
            name = 'CEVT/Vidp/' + sim_i + '_' + pos.replace('.mp4', extn)
            obj = html.Img(
                src=app.get_asset_url(name),
                style={"height": "50vh", "display": "block", "margin": "auto"}
                # , controls=True, autoPlay=True, #, type='video/mp4'
                ),
        else:
            name = c_i.replace('POS', pos)
            obj = html.Img(
                src=name,
                style={"height": "40vh", "display": "block", "margin": "auto"}
                ),        
        return(obj, txt, txt2, name, None, None)
    return(None, txt, txt2, None, None, None)


if __name__ == '__main__':
    app.run_server(debug=True)
