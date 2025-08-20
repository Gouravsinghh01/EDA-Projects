Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/backup/projects/3.EDA- Project-IPL/IPL.py
Matches DataFrame shape: (1095, 20)
Deliveries DataFrame shape: (260920, 17)

Matches DataFrame columns: ['id', 'season', 'city', 'date', 'match_type', 'player_of_match', 'venue', 'team1', 'team2', 'toss_winner', 'toss_decision', 'winner', 'result', 'result_margin', 'target_runs', 'target_overs', 'super_over', 'method', 'umpire1', 'umpire2']

Warning (from warnings module):
  File "C:/backup/projects/3.EDA- Project-IPL/IPL.py", line 35
    sns.barplot(x=wins.index, y=wins.values, palette="viridis")
FutureWarning: 

Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.


Warning (from warnings module):
  File "C:/backup/projects/3.EDA- Project-IPL/IPL.py", line 39
    plt.tight_layout()
UserWarning: Glyph 127942 (\N{TROPHY}) missing from font(s) Arial.

Warning (from warnings module):
  File "C:\Program Files\Python311\Lib\tkinter\__init__.py", line 861
    func(*args)
UserWarning: Glyph 127942 (\N{TROPHY}) missing from font(s) Arial.
Traceback (most recent call last):
  File "C:\Users\wwwra\AppData\Roaming\Python\Python311\site-packages\pandas\core\indexes\base.py", line 3805, in get_loc
    return self._engine.get_loc(casted_key)
  File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas\\_libs\\hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'win_by_runs'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:/backup/projects/3.EDA- Project-IPL/IPL.py", line 44, in <module>
    sns.histplot(matches['win_by_runs'], bins=30, kde=True, color='orange')
  File "C:\Users\wwwra\AppData\Roaming\Python\Python311\site-packages\pandas\core\frame.py", line 4102, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\wwwra\AppData\Roaming\Python\Python311\site-packages\pandas\core\indexes\base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: 'win_by_runs'

============= RESTART: C:/backup/projects/3.EDA- Project-IPL/IPL.py ============
Matches DataFrame shape: (1095, 20)
Deliveries DataFrame shape: (260920, 17)

Matches DataFrame columns: ['id', 'season', 'city', 'date', 'match_type', 'player_of_match', 'venue', 'team1', 'team2', 'toss_winner', 'toss_decision', 'winner', 'result', 'result_margin', 'target_runs', 'target_overs', 'super_over', 'method', 'umpire1', 'umpire2']
Warning: 'win_by_runs' column not found. Skipping plot.
Warning: 'win_by_wickets' column not found. Skipping plot.

Toss Impact: 50.59% of toss winners also won the match.

Warning (from warnings module):
  File "C:/backup/projects/3.EDA- Project-IPL/IPL.py", line 76
    sns.countplot(data=matches, x='toss_decision', palette='pastel')
FutureWarning: 

Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.


Warning (from warnings module):
  File "C:/backup/projects/3.EDA- Project-IPL/IPL.py", line 79
    plt.tight_layout()
UserWarning: Glyph 127919 (\N{DIRECT HIT}) missing from font(s) Arial.

Warning (from warnings module):
  File "C:\Program Files\Python311\Lib\tkinter\__init__.py", line 861
    func(*args)
UserWarning: Glyph 127919 (\N{DIRECT HIT}) missing from font(s) Arial.
Traceback (most recent call last):
  File "C:/backup/projects/3.EDA- Project-IPL/IPL.py", line 84, in <module>
    top_scorers = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)
  File "C:\Users\wwwra\AppData\Roaming\Python\Python311\site-packages\pandas\core\frame.py", line 9183, in groupby
    return DataFrameGroupBy(
  File "C:\Users\wwwra\AppData\Roaming\Python\Python311\site-packages\pandas\core\groupby\groupby.py", line 1329, in __init__
    grouper, exclusions, obj = get_grouper(
  File "C:\Users\wwwra\AppData\Roaming\Python\Python311\site-packages\pandas\core\groupby\grouper.py", line 1043, in get_grouper
    raise KeyError(gpr)
KeyError: 'batsman'

============= RESTART: C:/backup/projects/3.EDA- Project-IPL/IPL.py ============
Matches DataFrame shape: (1095, 20)
Deliveries DataFrame shape: (260920, 17)

Matches DataFrame columns: ['id', 'season', 'city', 'date', 'match_type', 'player_of_match', 'venue', 'team1', 'team2', 'toss_winner', 'toss_decision', 'winner', 'result', 'result_margin', 'target_runs', 'target_overs', 'super_over', 'method', 'umpire1', 'umpire2']
Warning: 'win_by_runs' column not found. Skipping plot.
Warning: 'win_by_wickets' column not found. Skipping plot.

Toss Impact: 50.59% of toss winners also won the match.
Warning: 'batsman' or 'batsman_runs' column not found. Skipping Top Run Scorers plot.

Warning (from warnings module):
  File "C:/backup/projects/3.EDA- Project-IPL/IPL.py", line 123
    sns.barplot(x=season_count.index, y=season_count.values, palette="mako")
FutureWarning: 

Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.


IPL EDA Completed.
>>> 
============= RESTART: C:/backup/projects/3.EDA- Project-IPL/IPL.py ============
Matches DataFrame shape: (1095, 20)
Deliveries DataFrame shape: (260920, 17)

Matches DataFrame columns: ['id', 'season', 'city', 'date', 'match_type', 'player_of_match', 'venue', 'team1', 'team2', 'toss_winner', 'toss_decision', 'winner', 'result', 'result_margin', 'target_runs', 'target_overs', 'super_over', 'method', 'umpire1', 'umpire2']
Warning: 'win_by_runs' column not found. Skipping plot.
Warning: 'win_by_wickets' column not found. Skipping plot.

Toss Impact: 50.59% of toss winners also won the match.
Warning: 'batsman' or 'batsman_runs' column not found. Skipping Top Run Scorers plot.

IPL EDA Completed.
