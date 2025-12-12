from datetime import datetime, timezone
gmt_dt = datetime.now(timezone.utc)
import random
from models.model_match import Match
from models.exceptions import ValidationError
from data.data_api import DataApi

GAME_TIMES = ["08:00", "09:30", "11:00", "12:30", "14:00", "15:30", "17:00", "18:30"]
MAX_GAMES_PER_DAY = len(GAME_TIMES)

class MatchLogic:
    """Handles all match related logic."""
    def __init__(self, data_api: DataApi) -> None:
        self._data_api = data_api

    def create_match(self,
        tournament_id: int,
        round_name: str,
        match_number: int,
        team_a_name: str,
        team_b_name: str,
        match_date: str,
        match_time: str,
        server_id: str,
        ) -> Match:
        """Creates a new match between two teams."""

        # Checks if user chooses same team twice
        if team_a_name == team_b_name:
            raise ValidationError("Ekki er hægt að velja sama liðið tvisvar.")

        # Checks all teams and raises errors if team doesn't exist
        all_teams = self._data_api.read_all_teams()
        team_a_exists = any(team.team_name == team_a_name for team in all_teams)
        team_b_exists = any(team.team_name == team_b_name for team in all_teams)

        if not team_a_exists:
            raise ValidationError(f"Liðið '{team_a_name}' er ekki á skrá.")
        if not team_b_exists:
            raise ValidationError(f"Liðið '{team_b_name}' er ekki á skrá.")
        
        # Loads existing matches
        all_matches = self._data_api.read_all_matches()

        # Checks the highest existing Id to assign new Id to new match
        existing_ids = []
        for match in all_matches:
            existing_ids.append(match.match_id)
        
        highest_id = max(existing_ids)
        new_id = highest_id + 1

        new_match = Match(
            match_id = new_id,
            tournament_id = tournament_id,
            round = round_name,
            match_number = match_number,
            team_a_name = team_a_name,
            team_b_name = team_b_name,
            match_date = match_date,
            match_time = match_time,
            server_id = server_id,
            score_a = 0,
            score_b = 0,
            winner_team_name = "",
            completed = False,
        )

        matches = self._data_api.read_all_matches()
        matches.append(new_match)
        self._data_api.save_all_matches(matches)

        return new_match
    
    def generate_round_of_16(self, tournament_id: int, team_names: list[str]):
        """Generate first 8 matches of tournament (R16)"""
        if len(team_names) != 16:
            raise ValueError("Einungis 16 lið geta verið í keppninni")
        
        matches = self._data_api.read_all_matches()

        for m in matches:
            if m.tournament_id == tournament_id and m.round == "16":
                return
            
        teams = team_names[:]
        random.shuffle(teams)

        next_id = self._get_next_match_id()

        new_matches: list[Match] = []

        for i in range(8):
            team_a = teams[2 * i]
            team_b = teams[2 * i + 1]

            match = Match(
                match_id=next_id,
                tournament_id=tournament_id,
                round="R16",
                match_number=i + 1,
                team_a_name=team_a,
                team_b_name=team_b,
                match_date="1",
                match_time=GAME_TIMES[i],
                server_id=str(i + 1),
                score_a=0,
                score_b=0,
                winner_team_name="",
                completed=False,
            )
            new_matches.append(match)
            next_id += 1
        
        matches.extend(new_matches)
        self._data_api.save_all_matches(matches)
    
    def generate_quarterfinals(self, tournament_id: int):
        """Generate next 4 rounds of the winners of round R16"""
        matches = self._data_api.read_all_matches()

        for m in matches:
            if m.tournament_id == tournament_id and m.round == "QF":
                return
            
        r16_matches = [m for m in matches if m.tournament_id == tournament_id and m.round == "R16"]
        completed_r16 = [m for m in r16_matches if m.completed]
        if len(completed_r16) != 8:
            raise ValidationError("Það þarf að klára alla 8 fyrstu leikina fyrst.")
        
        def r16_sort_key(m):
            return m.match_number
        completed_r16.sort(key=r16_sort_key)

        winners = [m.winner_team_name for m in completed_r16]

        next_id = self._get_next_match_id()
        new_matches: list[Match] = []

        for i in range(4):
            team_a = winners[2 * i]
            team_b = winners[2 * i + 1]
            match_number = 9 + i

            match2 = Match(
                match_id = next_id,
                tournament_id = tournament_id,
                round = "QF",
                match_number = match_number,
                team_a_name = team_a,
                team_b_name = team_b,
                match_date = "2",
                match_time = GAME_TIMES[i],
                server_id = str(match_number),
                score_a = 0,
                score_b = 0,
                winner_team_name = "",
                completed = False
            )

            new_matches.append(match2)
            next_id += 1
        
        matches.extend(new_matches)
        self._data_api.save_all_matches(matches)

    def generate_semifinals(self, tournament_id: int):
            """Generate round SF, of winners of QF"""
            matches = self._data_api.read_all_matches()

            for m in matches:
                if m.tournament_id == tournament_id and m.round == "SF":
                    return
            
            qf_matches = [
                m for m in matches
                if m.tournament_id == tournament_id and m.round == "QF"
            ]
            completed_qf = [m for m in qf_matches if m.completed]
            if len(completed_qf) != 4:
                raise ValidationError(f"Það þarf að klára alla síðustu 4 leiki ")
            
            def qf_sort_key(m):
                return m.match_number
            completed_qf.sort(key=qf_sort_key)

            winners = [m.winner_team_name for m in completed_qf]

            next_id = self._get_next_match_id()
            new_matches: list[Match] = []

            for i in range (2):
                team_a = winners[2 * i]
                team_b = winners[2 * i + 1]
                match_number = 13 + i

                match3 = Match(
                    match_id = next_id,
                    tournament_id = tournament_id,
                    round = "SF",
                    match_number = match_number,
                    team_a_name = team_a,
                    team_b_name = team_b,
                    match_date = "2",
                    match_time = GAME_TIMES[4 + i],
                    server_id = str(match_number),
                    score_a = 0,
                    score_b = 0,
                    winner_team_name = "",
                    completed = False
                )
                new_matches.append(match3)
                next_id += 1
        
            matches.extend(new_matches)
            self._data_api.save_all_matches(matches)

    def generate_final(self, tournament_id: int):
        """Generate final game"""
        matches = self._data_api.read_all_matches()

        for m in matches:
                if m.tournament_id == tournament_id and m.round == "F":
                    return
                
        sf_matches = [
                m for m in matches
                if m.tournament_id == tournament_id and m.round == "SF"
            ]
        completed_sf = [m for m in sf_matches if m.completed]
        if len(completed_sf) != 4:
            raise ValidationError(f"Það þarf að klára síðustu 2 leiki ")
        
        def sf_sort_key(m):
            return m.match_number
        completed_sf.sort(key=sf_sort_key)

        winners = [m.winner_team_name for m in completed_sf]
        next_id = self._get_next_match_id()

        final_match = Match(
            match_id=next_id,
            tournament_id=tournament_id,
            round="F",
            match_number=15,
            team_a_name=winners[0],
            team_b_name=winners[1],
            match_date="3",
            match_time=GAME_TIMES[0],
            server_id="15",
            score_a=0,
            score_b=0,
            winner_team_name="",
            completed=False,
        )

        matches.append(final_match)
        self._data_api.save_all_matches(matches)
            
    
    def get_matches_for_tournament(self, tournament_id: int) -> list[Match]:
        all_matches = self._data_api.read_all_matches()
        return [m for m in all_matches if m.tournament_id == tournament_id]
    
    def record_match_result(self, match_id: int, score_a: int, score_b: int) -> None:
        if score_a == score_b:
            raise ValidationError("Leikur má ekki enda með jafntefli í útsláttarkeppni.")
        
        matches = self._data_api.read_all_matches()

        target = None
        for m in matches:
            if m.match_id == match_id:
                target = m
                break
        
        if target is None:
            raise ValidationError(f"Leikur með id {match_id} fannst ekki.")
        
        target.score_a = score_a
        target.score_b = score_b
        winner = target.team_a_name if score_a > score_b else target.team_b_name
        target.winner_team_name = winner
        target.completed = True

        self._data_api.save_all_matches(matches)

    def _get_next_match_id(self) -> int:
        matches = self._data_api.read_all_matches()
        if not matches:
            return 1
        ids = [m.match_id for m in matches]
        return max(ids) + 1
