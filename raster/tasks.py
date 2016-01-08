import shutil
import traceback

from celery import task

from raster.tiles.parser import RasterLayerParser


@task
def create_tiles(rasterlayer, zoom):
    """
    Create all tiles for a raster layer at the input zoom level.
    """
    try:
        parser = RasterLayerParser(rasterlayer)
        parser.open_raster_file()
        parser.compute_max_zoom()
        parser.create_tiles(zoom)
    except:
        parser.log(
            traceback.format_exc(),
            status=parser.rasterlayer.parsestatus.FAILED
        )
        raise
    finally:
        shutil.rmtree(parser.tmpdir)


@task
def clear_tiles(rasterlayer):
    """
    Drop all tiles of a rasterlayer.
    """
    parser = RasterLayerParser(rasterlayer)
    parser.drop_all_tiles()


@task
def send_success_signal(rasterlayer):
    """
    Drop empty tiles of a raster layer and send parse succes signal.
    """
    parser = RasterLayerParser(rasterlayer)
    parser.drop_empty_tiles()
    parser.send_success_signal()


@task
def open_and_reproject_raster(rasterlayer, initial=False):
    """
    Initializes parser, creates reprojected raster copy if necessary.
    """
    try:
        parser = RasterLayerParser(rasterlayer)
        if initial:
            parser.log('Started parsing raster.')
        parser.open_raster_file()
    except:
        parser.log(
            traceback.format_exc(),
            status=parser.rasterlayer.parsestatus.FAILED
        )
        raise
    finally:
        shutil.rmtree(parser.tmpdir)
