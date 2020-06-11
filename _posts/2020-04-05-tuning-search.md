---
title:  "Song Order - Guitar Tunings and the Travelling Salesperson"
tags: music math cs
---

I play gigs with my acoustic guitar every now and then, and a lot of the pieces I play feature **weird** tunings. So here's the problem: tuning from one tuning to another very different tuning not only takes a long time, it makes the guitar go out of tune more quickly and also increases the risk of broken strings. Thus I want to order my songs such that the total amount of tuning I have to do is minimized.

## Definitions
Let's start with some definitions!
* Associate each key on the piano with an integer starting with A0 = 0, Bb0 = 1... and so on.
* Define a tuning to be a vector a 6 pitches.
* For any tunings x, y define their distance to be the *'manhattan distance'* or \\(L_1\\) distance:

$$d\_{tuning}(x, y) = \sum\_{i=1}^6 |x\_i - y\_i|.$$

Here it is in the rust language.

```rust
enum Note {A, Bb, B, C, Db, D, Eb, E, F, Gb, G, Ab}

struct Pitch(Note, i32); // Note, Octave

type Tuning = [Pitch; 6];
```

So to start, we have the `Notes` type which can take on one of 12 values. Then, we have the `Pitch` type which is represented as a tuple containing a `Note` and an octave, e.g. A4. We associate `Pitch` values with integers, and define distances as follows.

```rust
fn note2num(note: &Note) -> i32 {
    match note {
        Note::A => 0,
        Note::Bb => 1,
        Note::B => 2,
        ...
        Note::Ab => 11,
    }
}

impl Pitch {
    fn num(&self) -> i32 {
        note2num(&self.0) + (self.1 * 12)
    }
}

fn pitch_dist(p1: &Pitch, p2: &Pitch) -> i32 {
    (p1.num() - p2.num()).abs()
}

fn tuning_dist(p1: &Tuning, p2: &Tuning) -> i32 {
    p1.iter()
        .zip(p2)
        .map(|(a, b)| pitch_dist(a, b))
        .sum::< i32>()
}
```

## The Problem

Let's view this as a graph problem. Let the nodes in the graph be the tunings, and have an edge between each node, with the cost of the edge being the distance between the two tunings. Then **we want to find the 'shortest' path that passes through all the nodes**. Not only that, because we want to start and end up in standard tuning, we want to find the 'shortest' **cycle** that passes through all the nodes. **Turns out, this is a famous problem known as the travelling salesperson problem (TSP)**! And it's pretty hard to solve (NP-Hard). Here's what the problem looks like in 2 dimension (if we only had 2 strings): Try to find a cycle of shortest length while only being allowed to follow the grid.


<script type="text/javascript">window.PlotlyConfig = {MathJaxConfig: 'local'};</script>
<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>    
<div id="95301a00-ba5c-49e0-8b5c-34428713a00d" class="plotly-graph-div" style="height:100%; width:40%;"></div>
<script type="text/javascript">
    window.PLOTLYENV=window.PLOTLYENV || {};
    if (document.getElementById("95301a00-ba5c-49e0-8b5c-34428713a00d")) {
        Plotly.newPlot(
            '95301a00-ba5c-49e0-8b5c-34428713a00d',
            [{"hovertemplate": "first_string=%{x}<br>second_string=%{y}<br>size=%{marker.size}<extra></extra>", "legendgroup": "", "marker": {"color": "#636efa", "size": [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], "sizemode": "area", "sizeref": 0.01, "symbol": "circle"}, "mode": "markers", "name": "", "orientation": "v", "showlegend": false, "type": "scatter", "x": [2, 4, 5, 4, 3, 1, 4, 4, 6, 6, 3], "xaxis": "x", "y": [4, 1, 3, 2, 5, 1, 6, 4, 1, 6, 3], "yaxis": "y"}],
            {"legend": {"itemsizing": "constant", "tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "white", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "white", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "#C8D4E3", "linecolor": "#C8D4E3", "minorgridcolor": "#C8D4E3", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "#C8D4E3", "linecolor": "#C8D4E3", "minorgridcolor": "#C8D4E3", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "white", "showlakes": true, "showland": true, "subunitcolor": "#C8D4E3"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "white", "polar": {"angularaxis": {"gridcolor": "#EBF0F8", "linecolor": "#EBF0F8", "ticks": ""}, "bgcolor": "white", "radialaxis": {"gridcolor": "#EBF0F8", "linecolor": "#EBF0F8", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "white", "gridcolor": "#DFE8F3", "gridwidth": 2, "linecolor": "#EBF0F8", "showbackground": true, "ticks": "", "zerolinecolor": "#EBF0F8"}, "yaxis": {"backgroundcolor": "white", "gridcolor": "#DFE8F3", "gridwidth": 2, "linecolor": "#EBF0F8", "showbackground": true, "ticks": "", "zerolinecolor": "#EBF0F8"}, "zaxis": {"backgroundcolor": "white", "gridcolor": "#DFE8F3", "gridwidth": 2, "linecolor": "#EBF0F8", "showbackground": true, "ticks": "", "zerolinecolor": "#EBF0F8"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "#DFE8F3", "linecolor": "#A2B1C6", "ticks": ""}, "baxis": {"gridcolor": "#DFE8F3", "linecolor": "#A2B1C6", "ticks": ""}, "bgcolor": "white", "caxis": {"gridcolor": "#DFE8F3", "linecolor": "#A2B1C6", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "#EBF0F8", "linecolor": "#EBF0F8", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "#EBF0F8", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "#EBF0F8", "linecolor": "#EBF0F8", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "#EBF0F8", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "dtick": 1, "gridcolor": "lightgray", "gridwidth": 2, "showgrid": true, "showticklabels": false, "tick0": 0, "title": {"text": ""}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "dtick": 1, "gridcolor": "lightgray", "gridwidth": 2, "showgrid": true, "showticklabels": false, "tick0": 0, "title": {"text": ""}}},
            {"responsive": true}
        )
    };
    
</script>


What was the shortest cycle you could find? In this example, the solution is below with length 28.

<script type="text/javascript">window.PlotlyConfig={MathJaxConfig:"local"}</script><script src="https://cdn.plot.ly/plotly-latest.min.js"></script><div id="98b4fca2-9956-4066-ad5b-124fa3772b5b" class="plotly-graph-div" style="height:100%;width:40%"></div><script type="text/javascript">window.PLOTLYENV=window.PLOTLYENV||{},document.getElementById("98b4fca2-9956-4066-ad5b-124fa3772b5b")&&Plotly.newPlot("98b4fca2-9956-4066-ad5b-124fa3772b5b",[{hovertemplate:"first_string=%{x}<br>second_string=%{y}<br>size=%{marker.size}<br>ord=%{text}<extra></extra>",legendgroup:"",marker:{color:"#636efa",size:[4,4,4,4,4,4,4,4,4,4,4],sizemode:"area",sizeref:.01,symbol:"circle"},mode:"markers+text",name:"",orientation:"v",showlegend:!1,text:[0,6,4,5,1,8,2,10,7,3,9],textfont:{size:20},type:"scatter",x:[2,4,5,4,3,1,4,4,6,6,3],xaxis:"x",y:[4,1,3,2,5,1,6,4,1,6,3],yaxis:"y"}],{legend:{itemsizing:"constant",tracegroupgap:0},margin:{t:60},template:{data:{bar:[{error_x:{color:"#2a3f5f"},error_y:{color:"#2a3f5f"},marker:{line:{color:"white",width:.5}},type:"bar"}],barpolar:[{marker:{line:{color:"white",width:.5}},type:"barpolar"}],carpet:[{aaxis:{endlinecolor:"#2a3f5f",gridcolor:"#C8D4E3",linecolor:"#C8D4E3",minorgridcolor:"#C8D4E3",startlinecolor:"#2a3f5f"},baxis:{endlinecolor:"#2a3f5f",gridcolor:"#C8D4E3",linecolor:"#C8D4E3",minorgridcolor:"#C8D4E3",startlinecolor:"#2a3f5f"},type:"carpet"}],choropleth:[{colorbar:{outlinewidth:0,ticks:""},type:"choropleth"}],contour:[{colorbar:{outlinewidth:0,ticks:""},colorscale:[[0,"#0d0887"],[.1111111111111111,"#46039f"],[.2222222222222222,"#7201a8"],[.3333333333333333,"#9c179e"],[.4444444444444444,"#bd3786"],[.5555555555555556,"#d8576b"],[.6666666666666666,"#ed7953"],[.7777777777777778,"#fb9f3a"],[.8888888888888888,"#fdca26"],[1,"#f0f921"]],type:"contour"}],contourcarpet:[{colorbar:{outlinewidth:0,ticks:""},type:"contourcarpet"}],heatmap:[{colorbar:{outlinewidth:0,ticks:""},colorscale:[[0,"#0d0887"],[.1111111111111111,"#46039f"],[.2222222222222222,"#7201a8"],[.3333333333333333,"#9c179e"],[.4444444444444444,"#bd3786"],[.5555555555555556,"#d8576b"],[.6666666666666666,"#ed7953"],[.7777777777777778,"#fb9f3a"],[.8888888888888888,"#fdca26"],[1,"#f0f921"]],type:"heatmap"}],heatmapgl:[{colorbar:{outlinewidth:0,ticks:""},colorscale:[[0,"#0d0887"],[.1111111111111111,"#46039f"],[.2222222222222222,"#7201a8"],[.3333333333333333,"#9c179e"],[.4444444444444444,"#bd3786"],[.5555555555555556,"#d8576b"],[.6666666666666666,"#ed7953"],[.7777777777777778,"#fb9f3a"],[.8888888888888888,"#fdca26"],[1,"#f0f921"]],type:"heatmapgl"}],histogram:[{marker:{colorbar:{outlinewidth:0,ticks:""}},type:"histogram"}],histogram2d:[{colorbar:{outlinewidth:0,ticks:""},colorscale:[[0,"#0d0887"],[.1111111111111111,"#46039f"],[.2222222222222222,"#7201a8"],[.3333333333333333,"#9c179e"],[.4444444444444444,"#bd3786"],[.5555555555555556,"#d8576b"],[.6666666666666666,"#ed7953"],[.7777777777777778,"#fb9f3a"],[.8888888888888888,"#fdca26"],[1,"#f0f921"]],type:"histogram2d"}],histogram2dcontour:[{colorbar:{outlinewidth:0,ticks:""},colorscale:[[0,"#0d0887"],[.1111111111111111,"#46039f"],[.2222222222222222,"#7201a8"],[.3333333333333333,"#9c179e"],[.4444444444444444,"#bd3786"],[.5555555555555556,"#d8576b"],[.6666666666666666,"#ed7953"],[.7777777777777778,"#fb9f3a"],[.8888888888888888,"#fdca26"],[1,"#f0f921"]],type:"histogram2dcontour"}],mesh3d:[{colorbar:{outlinewidth:0,ticks:""},type:"mesh3d"}],parcoords:[{line:{colorbar:{outlinewidth:0,ticks:""}},type:"parcoords"}],pie:[{automargin:!0,type:"pie"}],scatter:[{marker:{colorbar:{outlinewidth:0,ticks:""}},type:"scatter"}],scatter3d:[{line:{colorbar:{outlinewidth:0,ticks:""}},marker:{colorbar:{outlinewidth:0,ticks:""}},type:"scatter3d"}],scattercarpet:[{marker:{colorbar:{outlinewidth:0,ticks:""}},type:"scattercarpet"}],scattergeo:[{marker:{colorbar:{outlinewidth:0,ticks:""}},type:"scattergeo"}],scattergl:[{marker:{colorbar:{outlinewidth:0,ticks:""}},type:"scattergl"}],scattermapbox:[{marker:{colorbar:{outlinewidth:0,ticks:""}},type:"scattermapbox"}],scatterpolar:[{marker:{colorbar:{outlinewidth:0,ticks:""}},type:"scatterpolar"}],scatterpolargl:[{marker:{colorbar:{outlinewidth:0,ticks:""}},type:"scatterpolargl"}],scatterternary:[{marker:{colorbar:{outlinewidth:0,ticks:""}},type:"scatterternary"}],surface:[{colorbar:{outlinewidth:0,ticks:""},colorscale:[[0,"#0d0887"],[.1111111111111111,"#46039f"],[.2222222222222222,"#7201a8"],[.3333333333333333,"#9c179e"],[.4444444444444444,"#bd3786"],[.5555555555555556,"#d8576b"],[.6666666666666666,"#ed7953"],[.7777777777777778,"#fb9f3a"],[.8888888888888888,"#fdca26"],[1,"#f0f921"]],type:"surface"}],table:[{cells:{fill:{color:"#EBF0F8"},line:{color:"white"}},header:{fill:{color:"#C8D4E3"},line:{color:"white"}},type:"table"}]},layout:{annotationdefaults:{arrowcolor:"#2a3f5f",arrowhead:0,arrowwidth:1},coloraxis:{colorbar:{outlinewidth:0,ticks:""}},colorscale:{diverging:[[0,"#8e0152"],[.1,"#c51b7d"],[.2,"#de77ae"],[.3,"#f1b6da"],[.4,"#fde0ef"],[.5,"#f7f7f7"],[.6,"#e6f5d0"],[.7,"#b8e186"],[.8,"#7fbc41"],[.9,"#4d9221"],[1,"#276419"]],sequential:[[0,"#0d0887"],[.1111111111111111,"#46039f"],[.2222222222222222,"#7201a8"],[.3333333333333333,"#9c179e"],[.4444444444444444,"#bd3786"],[.5555555555555556,"#d8576b"],[.6666666666666666,"#ed7953"],[.7777777777777778,"#fb9f3a"],[.8888888888888888,"#fdca26"],[1,"#f0f921"]],sequentialminus:[[0,"#0d0887"],[.1111111111111111,"#46039f"],[.2222222222222222,"#7201a8"],[.3333333333333333,"#9c179e"],[.4444444444444444,"#bd3786"],[.5555555555555556,"#d8576b"],[.6666666666666666,"#ed7953"],[.7777777777777778,"#fb9f3a"],[.8888888888888888,"#fdca26"],[1,"#f0f921"]]},colorway:["#636efa","#EF553B","#00cc96","#ab63fa","#FFA15A","#19d3f3","#FF6692","#B6E880","#FF97FF","#FECB52"],font:{color:"#2a3f5f"},geo:{bgcolor:"white",lakecolor:"white",landcolor:"white",showlakes:!0,showland:!0,subunitcolor:"#C8D4E3"},hoverlabel:{align:"left"},hovermode:"closest",mapbox:{style:"light"},paper_bgcolor:"white",plot_bgcolor:"white",polar:{angularaxis:{gridcolor:"#EBF0F8",linecolor:"#EBF0F8",ticks:""},bgcolor:"white",radialaxis:{gridcolor:"#EBF0F8",linecolor:"#EBF0F8",ticks:""}},scene:{xaxis:{backgroundcolor:"white",gridcolor:"#DFE8F3",gridwidth:2,linecolor:"#EBF0F8",showbackground:!0,ticks:"",zerolinecolor:"#EBF0F8"},yaxis:{backgroundcolor:"white",gridcolor:"#DFE8F3",gridwidth:2,linecolor:"#EBF0F8",showbackground:!0,ticks:"",zerolinecolor:"#EBF0F8"},zaxis:{backgroundcolor:"white",gridcolor:"#DFE8F3",gridwidth:2,linecolor:"#EBF0F8",showbackground:!0,ticks:"",zerolinecolor:"#EBF0F8"}},shapedefaults:{line:{color:"#2a3f5f"}},ternary:{aaxis:{gridcolor:"#DFE8F3",linecolor:"#A2B1C6",ticks:""},baxis:{gridcolor:"#DFE8F3",linecolor:"#A2B1C6",ticks:""},bgcolor:"white",caxis:{gridcolor:"#DFE8F3",linecolor:"#A2B1C6",ticks:""}},title:{x:.05},xaxis:{automargin:!0,gridcolor:"#EBF0F8",linecolor:"#EBF0F8",ticks:"",title:{standoff:15},zerolinecolor:"#EBF0F8",zerolinewidth:2},yaxis:{automargin:!0,gridcolor:"#EBF0F8",linecolor:"#EBF0F8",ticks:"",title:{standoff:15},zerolinecolor:"#EBF0F8",zerolinewidth:2}}},xaxis:{anchor:"y",domain:[0,1],dtick:1,gridcolor:"lightgray",gridwidth:2,showgrid:!0,showticklabels:!1,tick0:0,title:{text:""}},yaxis:{anchor:"x",domain:[0,1],dtick:1,gridcolor:"lightgray",gridwidth:2,showgrid:!0,showticklabels:!1,tick0:0,title:{text:""}}},{responsive:!0})</script>
        
<!-- <div id="98b4fca2-9956-4066-ad5b-124fa3772b5b" class="plotly-graph-div" style="height:100%; width:100%;"></div>
<script type="text/javascript">
window.PLOTLYENV=window.PLOTLYENV || {};
if (document.getElementById("98b4fca2-9956-4066-ad5b-124fa3772b5b")) {
    Plotly.newPlot(
        '98b4fca2-9956-4066-ad5b-124fa3772b5b',
        [{"hovertemplate": "first_string=%{x}<br>second_string=%{y}<br>size=%{marker.size}<br>ord=%{text}<extra></extra>", "legendgroup": "", "marker": {"color": "#636efa", "size": [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4], "sizemode": "area", "sizeref": 0.01, "symbol": "circle"}, "mode": "markers+text", "name": "", "orientation": "v", "showlegend": false, "text": [0.0, 6.0, 4.0, 5.0, 1.0, 8.0, 2.0, 10.0, 7.0, 3.0, 9.0], "textfont": {"size": 20}, "type": "scatter", "x": [2, 4, 5, 4, 3, 1, 4, 4, 6, 6, 3], "xaxis": "x", "y": [4, 1, 3, 2, 5, 1, 6, 4, 1, 6, 3], "yaxis": "y"}],
        {"legend": {"itemsizing": "constant", "tracegroupgap": 0}, "margin": {"t": 60}, "template": {"data": {"bar": [{"error_x": {"color": "#2a3f5f"}, "error_y": {"color": "#2a3f5f"}, "marker": {"line": {"color": "white", "width": 0.5}}, "type": "bar"}], "barpolar": [{"marker": {"line": {"color": "white", "width": 0.5}}, "type": "barpolar"}], "carpet": [{"aaxis": {"endlinecolor": "#2a3f5f", "gridcolor": "#C8D4E3", "linecolor": "#C8D4E3", "minorgridcolor": "#C8D4E3", "startlinecolor": "#2a3f5f"}, "baxis": {"endlinecolor": "#2a3f5f", "gridcolor": "#C8D4E3", "linecolor": "#C8D4E3", "minorgridcolor": "#C8D4E3", "startlinecolor": "#2a3f5f"}, "type": "carpet"}], "choropleth": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "choropleth"}], "contour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "contour"}], "contourcarpet": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "contourcarpet"}], "heatmap": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmap"}], "heatmapgl": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "heatmapgl"}], "histogram": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "histogram"}], "histogram2d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2d"}], "histogram2dcontour": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "histogram2dcontour"}], "mesh3d": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "type": "mesh3d"}], "parcoords": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "parcoords"}], "pie": [{"automargin": true, "type": "pie"}], "scatter": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter"}], "scatter3d": [{"line": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatter3d"}], "scattercarpet": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattercarpet"}], "scattergeo": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergeo"}], "scattergl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattergl"}], "scattermapbox": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scattermapbox"}], "scatterpolar": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolar"}], "scatterpolargl": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterpolargl"}], "scatterternary": [{"marker": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "type": "scatterternary"}], "surface": [{"colorbar": {"outlinewidth": 0, "ticks": ""}, "colorscale": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "type": "surface"}], "table": [{"cells": {"fill": {"color": "#EBF0F8"}, "line": {"color": "white"}}, "header": {"fill": {"color": "#C8D4E3"}, "line": {"color": "white"}}, "type": "table"}]}, "layout": {"annotationdefaults": {"arrowcolor": "#2a3f5f", "arrowhead": 0, "arrowwidth": 1}, "coloraxis": {"colorbar": {"outlinewidth": 0, "ticks": ""}}, "colorscale": {"diverging": [[0, "#8e0152"], [0.1, "#c51b7d"], [0.2, "#de77ae"], [0.3, "#f1b6da"], [0.4, "#fde0ef"], [0.5, "#f7f7f7"], [0.6, "#e6f5d0"], [0.7, "#b8e186"], [0.8, "#7fbc41"], [0.9, "#4d9221"], [1, "#276419"]], "sequential": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]], "sequentialminus": [[0.0, "#0d0887"], [0.1111111111111111, "#46039f"], [0.2222222222222222, "#7201a8"], [0.3333333333333333, "#9c179e"], [0.4444444444444444, "#bd3786"], [0.5555555555555556, "#d8576b"], [0.6666666666666666, "#ed7953"], [0.7777777777777778, "#fb9f3a"], [0.8888888888888888, "#fdca26"], [1.0, "#f0f921"]]}, "colorway": ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52"], "font": {"color": "#2a3f5f"}, "geo": {"bgcolor": "white", "lakecolor": "white", "landcolor": "white", "showlakes": true, "showland": true, "subunitcolor": "#C8D4E3"}, "hoverlabel": {"align": "left"}, "hovermode": "closest", "mapbox": {"style": "light"}, "paper_bgcolor": "white", "plot_bgcolor": "white", "polar": {"angularaxis": {"gridcolor": "#EBF0F8", "linecolor": "#EBF0F8", "ticks": ""}, "bgcolor": "white", "radialaxis": {"gridcolor": "#EBF0F8", "linecolor": "#EBF0F8", "ticks": ""}}, "scene": {"xaxis": {"backgroundcolor": "white", "gridcolor": "#DFE8F3", "gridwidth": 2, "linecolor": "#EBF0F8", "showbackground": true, "ticks": "", "zerolinecolor": "#EBF0F8"}, "yaxis": {"backgroundcolor": "white", "gridcolor": "#DFE8F3", "gridwidth": 2, "linecolor": "#EBF0F8", "showbackground": true, "ticks": "", "zerolinecolor": "#EBF0F8"}, "zaxis": {"backgroundcolor": "white", "gridcolor": "#DFE8F3", "gridwidth": 2, "linecolor": "#EBF0F8", "showbackground": true, "ticks": "", "zerolinecolor": "#EBF0F8"}}, "shapedefaults": {"line": {"color": "#2a3f5f"}}, "ternary": {"aaxis": {"gridcolor": "#DFE8F3", "linecolor": "#A2B1C6", "ticks": ""}, "baxis": {"gridcolor": "#DFE8F3", "linecolor": "#A2B1C6", "ticks": ""}, "bgcolor": "white", "caxis": {"gridcolor": "#DFE8F3", "linecolor": "#A2B1C6", "ticks": ""}}, "title": {"x": 0.05}, "xaxis": {"automargin": true, "gridcolor": "#EBF0F8", "linecolor": "#EBF0F8", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "#EBF0F8", "zerolinewidth": 2}, "yaxis": {"automargin": true, "gridcolor": "#EBF0F8", "linecolor": "#EBF0F8", "ticks": "", "title": {"standoff": 15}, "zerolinecolor": "#EBF0F8", "zerolinewidth": 2}}}, "xaxis": {"anchor": "y", "domain": [0.0, 1.0], "dtick": 1, "gridcolor": "lightgray", "gridwidth": 2, "showgrid": true, "showticklabels": false, "tick0": 0, "title": {"text": ""}}, "yaxis": {"anchor": "x", "domain": [0.0, 1.0], "dtick": 1, "gridcolor": "lightgray", "gridwidth": 2, "showgrid": true, "showticklabels": false, "tick0": 0, "title": {"text": ""}}},
        {"responsive": true}
    )
};
</script> -->
        

Our problem is just the same but the points are 6 dimensional instead of 2.
Here is the list of tunings we are working with (there are 14 of them).

```rust
[E2, A3, D3, G3, B3, E4]
[D2, A3, D3, G3, A3, D4]
[D2, A3, D3, Gb3, A3, D4]
[B2, E2, D3, Gb3, A3, D4]
[E2, B3, D3, G3, B3, D4]
[E2, B3, D3, G3, B3, E4]
[B2, Gb2, Db3, Gb3, B3, Gb4]
[E2, C3, D3, G3, A3, D4]
[D2, A3, D3, G3, C3, E4]
[C2, G2, D3, F3, Bb3, D4]
[Gb2, A3, B3, E3, Ab2, B4]
[Db2, Ab2, E3, Gb3, B3, Eb4]
[D2, A3, E3, F3, C3, E4]
[D2, G2, D3, G3, B3, E4]
```

## Brute Force Search
There are some really [cool algorithms for TSP](https://en.wikipedia.org/wiki/Travelling_salesman_problem#Computing_a_solution). But for my case, the simplest one - brute force - will suffice. This approach is to simply try every single cycle. We have 14 tunings, so how many cycles are there? Well because it's a cycle, it doesn't matter with which element it starts/ends with. So fix one, and then pick the order of the remaining 13 tunings (actually there are even fewer because the 'reverse cycle' has the same cost but I'll just ignore this). Thus we have \\(13! = 6,227,020,800\\) tunings cycles to look through! The brute force search algorithm is implemented here.

```rust
fn brute_force(tunings: &Vec<Tuning>) -> (i32, Vec<usize>) {
    let len = tunings.len();
    let first = &tunings[0];
    (1..len)
        .into_iter()
        .permutations(len - 1)
        .progress_count(fact((len as i32) - 1)) // Loading bar
        .map(|ord| (tuning_seq_dist_ord(tunings, &first, &ord), ord))
        .min_by_key(|x| x.0)
        .unwrap()
}
```

After running this, we found that the following cycle was optimal with weight 84 :)

```rust
[E2, A3, D3, G3, B3, E4]
[E2, B3, D3, G3, B3, E4]
[E2, B3, D3, G3, B3, D4]
[E2, C3, D3, G3, A3, D4]
[D2, A3, D3, G3, A3, D4]
[D2, A3, D3, Gb3, A3, D4]
[Gb2, A3, B3, E3, Ab2, B4]
[C2, G2, D3, F3, Bb3, D4]
[B2, E2, D3, Gb3, A3, D4]
[B2, Gb2, Db3, Gb3, B3, Gb4]
[Db2, Ab2, E3, Gb3, B3, Eb4]
[D2, A3, E3, F3, C3, E4]
[D2, A3, D3, G3, C3, E4]
[D2, G2, D3, G3, B3, E4]
[E2, A3, D3, G3, B3, E4]
```

Yay!