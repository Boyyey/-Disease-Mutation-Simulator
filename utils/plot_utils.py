import plotly.graph_objs as go

def get_custom_colorscale(name='reds'):
    """Return a custom Plotly colorscale."""
    if name == 'reds':
        return 'Reds'
    elif name == 'blues':
        return 'Blues'
    elif name == 'viridis':
        return 'Viridis'
    return 'Cividis'

def apply_plotly_theme(fig, theme='presentation'):
    """Apply a custom theme to a Plotly figure."""
    fig.update_layout(template=theme)
    return fig

def add_scientific_annotations(fig, text, x, y):
    """Add annotation to a Plotly figure."""
    fig.add_annotation(text=text, x=x, y=y, showarrow=True, arrowhead=1)
    return fig 