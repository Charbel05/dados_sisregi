import altair as alt
#import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import pandas as pd
alt.renderers.set_embed_options(actions=False)
def criar_grafico_horizontal(data, x, y, titulo, altura_personalizada=False, altura=None, com_borda = None):
    # Criar o gráfico
    base = alt.Chart(data).encode(
        x=alt.X(x),
        y=alt.Y(y).sort('-x').title(""),
        text=x
    )

    # Adicionar o título centralizado usando properties
    base = base.properties(
        title={
            "text": titulo,
            "anchor": 'middle'  # Centralizar o título
        }
    )

    fig = (base.mark_bar(cornerRadiusTopRight=10, cornerRadiusBottomRight=10, color="#153B8A") + base.mark_text(align='left', dx=2, color='black'))
    
    if altura_personalizada:
        # Atribuir a propriedade height diretamente ao objeto de gráfico
        fig = fig.properties(height=altura, width = altura * 4)

    if com_borda:
        # Configurar o fundo com gradiente radial (aplicado via CSS posteriormente)
        fig = fig.configure(background='rgba(207, 241, 255, 1)').configure_axis(labelLimit=120)
        
    else:
        fig = fig.configure(background="transparent").configure_axis(labelLimit=120)

    
    
  

    return fig

range_ = ['#FFDD00','#289048', '#009DE1', '#153B8A', '#FF4500','#289048', '#009688', '#FF1493', '#4B0082', '#00CED1', '#FF8C00']

def cria_grafico_pizza(dados, valor, legenda, titulo, rad, orient):
    base = alt.Chart(dados).mark_arc(innerRadius=rad).encode(
        theta=valor,
        color=alt.Color(legenda).scale(range=range_) 
    )

    base = base.properties(
         title={
            "text": titulo,
            "anchor": orient  # Centralizar o título
        }
    )
    base = base.properties(height=400)
    base = base.configure(background="transparent")  # Corrected the property name
    return base

#def cria_grafico_pizza_plotly(dados, valores, titulo, altura):
    #fig = go.Figure(data=[go.Pie(labels=dados, values=valores, textinfo='label+percent', insidetextorientation='radial')])
    #fig.update_layout(
    #    title=titulo,
    #    height=altura,
    #    title_x=0.5,
    #    title_y = 0.95,  # Centralizar o título horizontalmente
    #    title_xanchor='center',
    #   paper_bgcolor='rgba(0,0,0,0)'
    #)

    return fig

def criar_grafico_linhas(data, x, y, titulo, tamanho):
    # Criar o gráfico
    grafico = alt.Chart(data).mark_line(point=True).encode(
        x=x,
        y=y
    )

    # Adicionar o título centralizado usando properties
    grafico = grafico.properties(
        title={
            "text": titulo,
            "anchor": 'middle'  # Centralizar o título
        }
    )
    text = grafico.mark_text(align='center', baseline='middle', dy=-10).encode(
        text=y
    )
    grafico = grafico + text
    grafico=grafico.properties(height=tamanho, width = tamanho * 3)
    
    grafico=grafico.configure(background="transparent")
    return grafico

def criar_grafico_vertical(data, x, y, titulo, altura_personalizada=False, altura=None):
    # Criar o gráfico
    base = alt.Chart(data).encode(
        x=alt.X(x).sort('y'),
        y=alt.Y(y),
        text=y
    )

    # Adicionar o título centralizado usando properties
    base = base.properties(
        title={
            "text": titulo,
            "anchor": 'middle'  # Centralizar o título
        }
    )

    fig = (base.mark_bar(cornerRadiusTopRight=10, cornerRadiusTopLeft=10, color="#153B8A") + base.mark_text(align='center', dy=-10))
    
    if altura_personalizada:
        # Atribuir a propriedade height diretamente ao objeto de gráfico
        fig = fig.properties(height=altura)

    # Configurar o fundo transparente
    fig = fig.configure(background="transparent").configure_axis(labelLimit=1000)
  

    return fig
range_2 = ['#00CED1','#FFDD00','#289048', '#009DE1', '#153B8A', '#FF4500','#289048', '#009688', '#FF1493', '#4B0082', '#00CED1', '#FF8C00']
def criar_grafico_horizontal_segmento(data, x_1, y_1, titulo, segmento, titulosegmento, labellimit, altura_personalizada=False, altura=None):
    # Criar o gráfico
    base = alt.Chart(data).mark_bar(cornerRadiusTopRight=10, cornerRadiusBottomRight=10).encode(
        x=alt.X(f'sum({x_1}):Q').stack('zero'),
        y=alt.Y(f'{y_1}:N').sort('-x'),
        color=alt.Color(segmento, title=titulosegmento).scale(range=range_2) 
    )

    # Adicionar o título centralizado usando properties
    base = base.properties(
        title={
            "text": titulo,
            "anchor": 'middle'  # Centralizar o título
        }
    )

    text = alt.Chart(data).mark_text(dx=-15, dy=3, color='white').encode(
        x=alt.X(f'sum({x_1}):Q').stack('zero'),
        y=alt.Y(f'{y_1}:N').sort('-x'),
        detail=f'{segmento}:N',
        text=alt.Text(f'sum({x_1}):Q', format='.1f')  # Exibir os valores de y com 2 casas decimais
    )

    

    fig=base + text
    fig = fig.configure(background="transparent")


    

    if altura_personalizada:
        # Atribuir a propriedade height diretamente ao objeto de gráfico
        fig = fig.properties(height=altura)

    
    
    return fig

def cria_teste(data, x, y, color):

    bars = alt.Chart(data).mark_bar().encode(
        x=alt.X(f'sum({x}):Q').stack('zero'),
        y=alt.Y(f'{y}:N').sort('-x'),
        color=alt.Color(color)
    )

    text = alt.Chart(data).mark_text(dx=-15, dy=3, color='white').encode(
        x=alt.X(f'sum({x}):Q').stack('zero'),
        y=alt.Y(f'{y}:N').sort('-x'),
        detail=f'{color}:N',
        text=alt.Text(f'sum({x}):Q', format='.1f')
    )

    fig = bars + text
    return fig

def criar_grafico_varias_linhas(data, x, y, titulo, tamanho, color):
    # Criar o gráfico
    grafico = alt.Chart(data).mark_line(point=True).encode(
        x=x,
        y=y,
        color=alt.Color(color)
    )

    # Adicionar o título centralizado usando properties
    grafico = grafico.properties(
        title={
            "text": titulo,
            "anchor": 'middle'  # Centralizar o título
        }
    )
    text = grafico.mark_text(align='center', baseline='middle', dy=-10).encode(
        text=y
    )
    grafico = grafico + text
    grafico=grafico.properties(height=tamanho, width = tamanho * 3)
    grafico=grafico.configure(background="transparent")
    return grafico


def cria_tree_map(dados, paths, valor, altura):
    fig_2 = px.treemap(dados, path=paths, values=valor, color_discrete_sequence=['#E0F7FA', '#80DEEA', '#26C6DA', '#00ACC1'])

    fig_2.update_layout(
        height=altura,
        paper_bgcolor='rgba(0,0,0,0)',
        treemapcolorway=['#E0F7FA', '#80DEEA', '#26C6DA', '#00ACC1']
    )
    fig_2.update_traces(marker=dict(cornerradius=5), hoverinfo='label+value+text')
    fig_2.update_layout(margin=dict(t=0, l=10, r=10, b=10), font=dict(size=25))

    # Atualização do texttemplate para fazer quebras de linha automáticas
    fig_2.update_traces(texttemplate="%{label}<br>%{value}")

    return fig_2

import numpy as np

def imagens_produtividade_funicionarios(data, titulo):
    fig = criar_grafico_vertical(data,'Nome', 'Total', titulo,1, 700)


    b1 = np.percentile(data['Total'], 25)
    b2 = np.percentile(data['Total'], 50)
    b3 = np.percentile(data['Total'], 75)

    data['Comparacao'] = np.where(data['Total'] < b1, 'Menor que 50%',
                                    np.where(data['Total'] < b3, 'Menor que 75%', 'Maior que 75%'))


    lines = pd.DataFrame({'value': [b1, b2, b3], 'label': ['25%', '50%', '75%']})
    horizontal_lines = alt.Chart(lines).mark_rule(strokeDash=[3, 3]).encode(
        y='value:Q',
        color=alt.value('grey'),  # Cor das linhas
        tooltip='label',  # Rótulo para exibir no tooltip
        text = 'label'
    )

    text = horizontal_lines.mark_text(align='right', baseline='top', dy=-10, dx=-500).encode(
            text='label'
        )

    fig = fig + horizontal_lines + text

    fig = fig.encode(
        color=alt.Color("Comparacao:N", scale=alt.Scale(range=['green', 'red', 'blue'])),
    )
    return fig