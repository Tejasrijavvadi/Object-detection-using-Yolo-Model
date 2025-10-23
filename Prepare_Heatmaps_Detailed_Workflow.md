# Detailed cell-by-cell workflow for `Prepare_Heatmaps_Demo.ipynb`

## Cell 0 — Code (32 lines)
- First line: `import numpy as np`
- Detected actions: imports, plotting/visualization, ml_training/inference
- Source preview:
```
import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm
import seaborn as sns
...
```

## Cell 1 — Code (3 lines)
- First line: `#MIN/MAX Coordinates for Suncor's base plant mine`
- Detected actions: no obvious actions detected
- Source preview:
```
#MIN/MAX Coordinates for Suncor's base plant mine
YMIN, YMAX = 243303, 255704
XMIN, XMAX = 146900, 156672
```

## Cell 2 — Markdown
# Grid Class

## Cell 3 — Code (323 lines)
- First line: `class GridDef:`
- Detected actions: function_definition
- Source preview:
```
class GridDef:
    """
    Spatial grid definition class for fast conversion between coordinates and grid indices over a fixed spatial grid.
    
    The grid follows numpy array indexing conventions:
    - Grid[i, j] where i is row (Y direction) and j is column (X direction)
...
```

## Cell 4 — Markdown
Create grid for Suncor's Base Plant mine site. These won't change.

## Cell 5 — Code (16 lines)
- First line: `#--- Create bp_grid object representing the grid to build heatmaps on`
- Detected actions: no obvious actions detected
- Source preview:
```
#--- Create bp_grid object representing the grid to build heatmaps on
bp_grid = GridDef(x_min=XMIN, x_max=XMAX, y_min=YMIN, y_max=YMAX,
                  cell_size_x=10, cell_size_y=10)

#--- Create explicit array of coordinates for every cell of the grid (for plotting, etc)
grid_xcoords, grid_ycoords = [], []
...
```

## Cell 6 — Markdown
# Map matching

## Cell 7 — Code (413 lines)
- First line: `def build_activity_heatmap(`
- Detected actions: dataframe_creation, groupby/aggregation, function_definition
- Source preview:
```
def build_activity_heatmap(
    bp_grid: GridDef, #2D grid to create heatmap on
    df: pd.DataFrame, #Database with equipment records
    *,
    #Geometry columns - From equipment database
    start_x_col: str = "startpositionx",
...
```

## Cell 8 — Markdown
# Grader activity time heatmaps

## Cell 9 — Markdown
## Utilities

## Cell 10 — Code (41 lines)
- First line: `def check_graders_act_heatmap(hour_graders_df, heatmap, meta,`
- Detected actions: function_definition
- Source preview:
```
def check_graders_act_heatmap(hour_graders_df, heatmap, meta,
                              segmentduration_colname):
    """
    This function takes a graders records dataframe, a heatmap, meta information about the heatmap
    operation and checks that the heatmap correctly represents the total grader activity reported in
    the grader dataframe. The grader dataframe passed here MUST be the filtered one used for grader
...
```

## Cell 11 — Code (51 lines)
- First line: `def get_working_graders_df(graders_df: pd.DataFrame, start_tstamp: str, delta_hrs: int,`
- Detected actions: dataframe_creation, function_definition
- Source preview:
```
def get_working_graders_df(graders_df: pd.DataFrame, start_tstamp: str, delta_hrs: int,
                           speed_min: float, speed_max: float, xmin: float, xmax: float,
                           ymin: float, ymax: float, speed_colname: str, timestamp_colname: str,
                           maxduration_s:float, prod_time_label: str, prodtime_colname: str,
                           segmentduration_colname: str, startxcoord_colname: str, endxcoord_colname: str,
                           startycoord_colname: str, endycoord_colname: str,
...
```

## Cell 12 — Markdown
## DEMO

## Cell 13 — Markdown
Using the functions provided, every hour, we create a heatmap of grader activity for the past 4, 12 and 24 hours (or potentially other intervals in the future). The heatmap validation metrics must be computed and stored internally for our inspection as well.

## Cell 14 — Code (21 lines)
- First line: `#Pull data from DB or data source, here for demo I'm loading data from May`
- Detected actions: data_load
- Source preview:
```
#Pull data from DB or data source, here for demo I'm loading data from May
#NOTE: Suncor's equipment table has ALL equipment, need to extract graders records here by equipment type
graders_df = pd.read_csv("data/bp_graders_May_2025.csv")

#Convert timestamp fields to datetime timestamp format, check column name for timestamp fields
graders_df['GPSSTARTDATETIME'] = pd.to_datetime(graders_df['GPSSTARTDATETIME']).dt.tz_localize(None) #db data have tz, but can remove since everything in same Tzone
...
```

## Cell 15 — Code (24 lines)
- First line: `heatmap_sec, meta = build_activity_heatmap(`
- Detected actions: plotting/visualization
- Source preview:
```
heatmap_sec, meta = build_activity_heatmap(
    bp_grid, hour_graders_df,
    start_x_col='STARTPOSITIONXMETRES', start_y_col='STARTPOSITIONYMETRES',
    end_x_col='ENDPOSITIONXMETRES', end_y_col='ENDPOSITIONYMETRES',
    tstart_col='GPSSTARTDATETIME', tend_col='GPSENDDATETIME',
    equipment_col='EQUIPMENTUNITNAME',
...
```

## Cell 16 — Markdown
# Avg Speed Heatmaps

## Cell 17 — Code (21 lines)
- First line: `#The trucks dataframe is pretty large, here for the purpose of loading in local computer just a subset of columns`
- Detected actions: no obvious actions detected
- Source preview:
```
#The trucks dataframe is pretty large, here for the purpose of loading in local computer just a subset of columns
usecols = [
 'GPSSTARTDATETIME',
 'LOCATIONDETAILFOR',
 'EQUIPMENTUNITNAME',
 'EQUIPMENTMODELNAME',
...
```

## Cell 18 — Markdown
## Utilities

## Cell 19 — Code (57 lines)
- First line: `def get_working_trucks_df(trucks_df: pd.DataFrame, start_tstamp_str: str, delta_hrs: int,`
- Detected actions: dataframe_creation, function_definition
- Source preview:
```
def get_working_trucks_df(trucks_df: pd.DataFrame, start_tstamp_str: str, delta_hrs: int,
                           xmin: float, xmax: float, ymin: float, ymax: float, maxduration_s:float, speed_min: float,
                           speed_max: float, maxlength_m: float, cycletype: str, timestamp_colname: str, segmentduration_colname: str,
                           segmentlength_colname: str, startxcoord_colname: str, endxcoord_colname: str, speed_colname: str,
                           startycoord_colname: str, endycoord_colname: str, cycletype_colname: str,
                           print_time: bool = False):
...
```

## Cell 20 — Markdown
## DEMO

## Cell 21 — Markdown
Using the functions provided, every hour, we create a heatmap of grader activity for the past 4, 12 and 24 hours (or potentially other intervals in the future). The heatmap validation metrics must be computed and stored internally for our inspection as well.

## Cell 22 — Code (5 lines)
- First line: `trucks_df = pd.read_csv("data/bp_trucks_May_2025.csv", usecols=usecols) #care, big file ~8Gbs. May want to export a section to test demo`
- Detected actions: data_load
- Source preview:
```
trucks_df = pd.read_csv("data/bp_trucks_May_2025.csv", usecols=usecols) #care, big file ~8Gbs. May want to export a section to test demo

#Convert timestamp fields to datetime timestamp format, check column name for timestamp fields
trucks_df['GPSSTARTDATETIME'] = pd.to_datetime(trucks_df['GPSSTARTDATETIME']).dt.tz_localize(None)
trucks_df['GPSENDDATETIME'] = pd.to_datetime(trucks_df['GPSSTARTDATETIME']).dt.tz_localize(None)
```

## Cell 23 — Markdown
### Empty Truck Avg Speed

## Cell 24 — Code (9 lines)
- First line: `start_time_str = '2025-05-05 08:00:00'`
- Detected actions: no obvious actions detected
- Source preview:
```
start_time_str = '2025-05-05 08:00:00'
delta_hrs = 4

hour_trucks_empty_df = get_working_trucks_df(
    trucks_df, start_tstamp_str=start_time_str, delta_hrs=delta_hrs, xmin=XMIN, xmax=XMAX, ymin=YMIN, ymax=YMAX, speed_min=-70, speed_max=70, #consider trucks backing up, trucks can't go faster than ~60-65 kmh
    maxduration_s=25, maxlength_m=500, cycletype='Empty', timestamp_colname='GPSSTARTDATETIME', segmentduration_colname='SEGMENTDURATIONSECONDS',
...
```

## Cell 25 — Code (22 lines)
- First line: `heatmap_avg_speed_empty, meta_avg_speed_empty = build_activity_heatmap(`
- Detected actions: plotting/visualization
- Source preview:
```
heatmap_avg_speed_empty, meta_avg_speed_empty = build_activity_heatmap(
    bp_grid, hour_trucks_empty_df,
    start_x_col='STARTPOSITIONXMETRES', start_y_col='STARTPOSITIONYMETRES',
    end_x_col='ENDPOSITIONXMETRES', end_y_col='ENDPOSITIONYMETRES',
    tstart_col='GPSSTARTDATETIME', tend_col='GPSENDDATETIME',
    equipment_col='EQUIPMENTUNITNAME',
...
```

## Cell 26 — Markdown
### Loaded Truck Avg Speed

## Cell 27 — Code (9 lines)
- First line: `start_time_str = '2025-05-05 08:00:00'`
- Detected actions: no obvious actions detected
- Source preview:
```
start_time_str = '2025-05-05 08:00:00'
delta_hrs = 4

hour_trucks_loaded_df = get_working_trucks_df(
    trucks_df, start_tstamp_str=start_time_str, delta_hrs=delta_hrs, xmin=XMIN, xmax=XMAX, ymin=YMIN, ymax=YMAX, speed_min=-70, speed_max=70, #consider trucks backing up, trucks can't go faster than ~60-65 kmh
    maxduration_s=25, maxlength_m=500, cycletype='Loaded', timestamp_colname='GPSSTARTDATETIME', segmentduration_colname='SEGMENTDURATIONSECONDS',
...
```

## Cell 28 — Code (22 lines)
- First line: `heatmap_avg_speed_loaded, meta_avg_speed_loaded = build_activity_heatmap(`
- Detected actions: plotting/visualization
- Source preview:
```
heatmap_avg_speed_loaded, meta_avg_speed_loaded = build_activity_heatmap(
    bp_grid, hour_trucks_loaded_df,
    start_x_col='STARTPOSITIONXMETRES', start_y_col='STARTPOSITIONYMETRES',
    end_x_col='ENDPOSITIONXMETRES', end_y_col='ENDPOSITIONYMETRES',
    tstart_col='GPSSTARTDATETIME', tend_col='GPSENDDATETIME',
    equipment_col='EQUIPMENTUNITNAME',
...
```

## Cell 29 — Markdown
# Assembling CSV from heatmap np.arrays

## Cell 30 — Code (33 lines)
- First line: `def grid_to_dataframe(values, xcoords, ycoords, xsize, ysize):`
- Detected actions: dataframe_creation, function_definition
- Source preview:
```
def grid_to_dataframe(values, xcoords, ycoords, xsize, ysize):
    """
    Convert a 2D numpy grid with coordinate arrays into a flat DataFrame.

    Parameters
    ----------
...
```

## Cell 31 — Markdown
Note: The heatmaps are for a time interval so care when saving/loading depending on user time range selection (past 4 hours, 12 hours, 24 hours)

## Cell 32 — Code (7 lines)
- First line: `#grid_xcoords, grid_ycoords were created earlier in the notebook`
- Detected actions: no obvious actions detected
- Source preview:
```
#grid_xcoords, grid_ycoords were created earlier in the notebook
grader_act_df = grid_to_dataframe(heatmap_sec, grid_xcoords, grid_ycoords, xsize=bp_grid.cell_size_x, ysize=bp_grid.cell_size_y)
avg_empty_speed_df = grid_to_dataframe(heatmap_avg_speed_empty, grid_xcoords, grid_ycoords, xsize=bp_grid.cell_size_x, ysize=bp_grid.cell_size_y)

#filter out empty values (most of the grid cells are empty as equipment covers small fraction of actual site footprint)
grader_act_df = grader_act_df[~grader_act_df['value'].isna()]
...
```

## Cell 33 — Code (1 lines)
- First line: `grader_act_df.head()`
- Detected actions: no obvious actions detected
- Source preview:
```
grader_act_df.head()
```

## Cell 34 — Code (1 lines)
- First line: `avg_empty_speed_df.head()`
- Detected actions: no obvious actions detected
- Source preview:
```
avg_empty_speed_df.head()
```
