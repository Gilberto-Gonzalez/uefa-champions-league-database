def referees_without_matches(cursor):
    query = """
        SELECT Name
        FROM Referees
        WHERE RefereeID NOT IN (
            SELECT DISTINCT RefereeID FROM Matches
        )
    """
    cursor.execute(query)
    results = cursor.fetchall()

    # Clean the tuple to just get the name string
    return [(row[0],) for row in results]

def referees_without_matches(cursor):
    query = """
        SELECT Name
        FROM MainReferee
        WHERE MainRefereeID NOT IN (
            SELECT DISTINCT MainRefereeID FROM Match
        );
    """
    cursor.execute(query)
    return cursor.fetchall()

def players_born_2000_or_teams_after_2000(cursor):
    query = """
        SELECT Name FROM Player WHERE YEAR(DOB) >= 2000
        UNION
        SELECT P.Name
        FROM Player P
        JOIN Team T ON P.TeamID = T.TeamID
        WHERE T.FounderYear > 2000;
    """
    cursor.execute(query)
    return cursor.fetchall()

def top_goal_scorers(cursor):
    query = """
        SELECT TOP 5 P.Name, COUNT(*) AS Goals
        FROM Score S
        JOIN Player P ON S.PlayerID = P.PlayerID
        GROUP BY P.Name
        ORDER BY Goals DESC;
    """
    cursor.execute(query)
    return cursor.fetchall()

def team_goal_totals(cursor):
    query = """
        WITH TeamGoals AS (
            SELECT P.TeamID, COUNT(*) AS TotalGoals
            FROM Score S
            JOIN Player P ON S.PlayerID = P.PlayerID
            GROUP BY P.TeamID
        )
        SELECT T.Name, TG.TotalGoals
        FROM Team T
        JOIN TeamGoals TG ON T.TeamID = TG.TeamID
        ORDER BY TG.TotalGoals DESC;
    """
    cursor.execute(query)
    return cursor.fetchall()

def olap_goals_by_team_and_player(cursor):
    query = """
        SELECT 
            T.Name AS TeamName,
            COALESCE(P.Name, 'Total') AS PlayerName,
            COUNT(*) AS Goals
        FROM Score S
        JOIN Player P ON S.PlayerID = P.PlayerID
        JOIN Team T ON P.TeamID = T.TeamID
        GROUP BY ROLLUP (T.Name, P.Name);
    """
    cursor.execute(query)
    return cursor.fetchall()