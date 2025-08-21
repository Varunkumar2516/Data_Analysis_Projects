## 📊 Data Understanding

### Dataset Structure
- **Source:** Single CSV file containing ball-by-ball IPL match data.
- **One row** = one ball bowled (including extras such as wides and no-balls).
- **`match_id`** identifies the match each ball belongs to.
- Each match contains roughly ~200 rows:
  - **Inning 1:** ~120 balls (20 overs) or fewer if all out/innings closed early.
  - **Inning 2:** ~120 balls or fewer depending on result.

---

### Innings & Team Roles
- **Inning 1**:
  - `batting_team` = team batting first.
  - `bowling_team` = team bowling first.
  - Total runs scored in this inning = **target** for second innings.
- **Inning 2**:
  - Teams swap roles.
  - Runs scored determine if the target is chased or defended.

---

### Creating Match-Level Summary
Since there’s no separate matches file:
- Use `match_id` with `drop_duplicates()` (or `groupby`) to get one row per match.
- From the first ball of each match, extract details like:
  - Season/year
  - Teams playing (`batting_team` & `bowling_team` in inning 1)
  - Venue (if available in dataset)
- Aggregate runs per inning to determine results.

---

### Relation to Match Outcomes
- If `inning 2` total runs **≥** `inning 1` total → batting team in inning 2 wins.
- Otherwise → bowling team in inning 2 wins.
- This logic can be applied directly to the ball-by-ball dataset without external files.


1,180 total matches scheduled

– 11 abandoned matches
= 1,169 completed matches.