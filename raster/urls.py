from django.urls import re_path
from raster.views import AlgebraView, ExportView, LegendView

urlpatterns = [

    # Normal raster tiles endpoint
    re_path(
        r'^tiles/(?P<layer>[^/]+)/(?P<z>[0-9]+)/(?P<x>[0-9]+)/(?P<y>[0-9]+).(?P<frmt>png|jpg|tif)$',
        AlgebraView.as_view(),
        name='tms',
    ),

    # Raster algebra endpoint
    re_path(
        r'^algebra/(?P<z>[0-9]+)/(?P<x>[0-9]+)/(?P<y>[0-9]+).(?P<frmt>jpg|png|tif)$',
        AlgebraView.as_view(),
        name='algebra',
    ),

    # Pixel value endpoint
    re_path(
        r'^pixel/(?P<xcoord>-?\d+(?:\.\d+)?)/(?P<ycoord>-?\d+(?:\.\d+)?)$',
        AlgebraView.as_view(),
        name='pixel',
    ),

    # Raster legend endpoints.
    re_path(
        r'^legend$',
        LegendView.as_view(),
        name='legend',
    ),
    re_path(
        r'^legend/(?P<legend_id>[^/]+)$',
        LegendView.as_view(),
        name='legend-detail',
    ),

    # Exporter endpoint
    re_path(
        r'^export$',
        ExportView.as_view(),
        name='export',
    ),
]
