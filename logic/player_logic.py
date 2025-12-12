from data.data_api import DataApi
from models.model_player import Player
from models.exceptions import ValidationError
from datetime import datetime

class PlayerLogic:
    """Handles all player related logic."""

    def __init__(self, data_api: DataApi) -> None:
        self._data_api = data_api

    #------------------METHODS-THAT-GET-DATA------------------------
    
    def handle_exists(self, handle: str) -> bool:
        """Return True if player handle already exists."""
        players = self._data_api.read_all_players()
        handle_casefold = handle.casefold()
        return any(player.handle.casefold() == handle_casefold for player in players)

    def get_players_for_team(self, team_name: str) -> list[Player]:
        """Retrives all players whose team name matches the given team."""
        players = self._data_api.read_all_players()
        return [player for player in players if player.team_name == team_name]

    def get_list_of_all_players(self, all_players: list):
        """Gets a list of all players on file"""
        all_players = self._data_api.read_all_players()
        return all_players
    
    def validate_handle_format(self, handle: str) -> str:
        """Public wrapper so UI/LLApi can validate a handle."""
        return self._validate_handle_format(handle)

    #------------------METHODS-THAT-CHANGE-DATA----------------------
    def create_player(self,
        name: str,
        date_of_birth: str,
        address: str,
        phone: str,
        email: str,
        link: str,
        handle: str,
        team_name: str,
    ) -> Player:
        """Creates a new player in system."""

        # Validation
        name = self._validate_person_name(name)
        date_of_birth = self._validate_date_of_birth(date_of_birth)
        address = self._validate_address(address)
        phone = self._normalize_phone(phone)
        email = self._validate_email(email)
        handle = self._validate_handle_format(handle)
        link = self._normalize_player_link(link)

        # Checks if player already exists
        players = self._data_api.read_all_players()
        handle_casefold = handle.casefold()
        if any(player.handle.casefold() == handle_casefold for player in players):
            raise ValidationError("Leikmanna nafn (handle) er nú þegar á skrá.")

        # Creates new player_id
        if players:
            existing_player_nums = [int(player.player_id[1:]) for player in players]
            highest_num = max(existing_player_nums)
        else:
            highest_num = 0
        new_id = f"P{highest_num + 1:03d}"

        #Creates a new player object
        new_player = Player(
            player_id = new_id,
            name = name,
            date_of_birth = date_of_birth,
            address = address,
            phone = phone,
            email = email,
            link = link,
            handle = handle,
            team_name = team_name,
        )

        players.append(new_player)
        self._data_api.save_all_players(players)

        return new_player
    
    def update_player(self, update_player: Player) -> None:
        """ """
        players = self._data_api.read_all_players()

        for index, player in enumerate(players):
            if player.player_id == update_player.player_id:
                players[index] = update_player
                self._data_api.save_all_players(players)
                return
        
        raise ValidationError("Leikmaður með þetta auðkenni fannst ekki.")
    
    #------------------INTERNAL-HELPER-METHODS----------------------

    def _validate_person_name(self, name: str) -> str:
        n = name.strip()
        if not n:
            raise ValidationError("Þú verður að skrá nafn.")
        for ch in n:
            if ch.isalpha() or ch in {" ", "-"}:
                continue
            raise ValidationError("Nafn má bara innihalda bókstafi, bil og '-'.")
        return n
    
    def _validate_date_of_birth(self, dob_str: str) -> str:
        s = dob_str.strip()
        try:
            dob = datetime.strptime(s, "%Y-%m-%d").date()
        except ValueError:
            raise ValidationError("Fæðingardagur verður að vera á forminu YYYY-MM-DD (t.d. 1995-10-31).")
        if not (1926 <= dob.year <= 2007):
            raise ValidationError("Fæðingardagur verður að vera á bilinu 1926 til 2007.")
        return s
    
    def _validate_address(self, address: str) -> str:
        a = address.strip()
        if not a:
            raise ValidationError("Þú verður á skrá heimilisfang.")
        allowed_extra = {" ", "-", ",", "."}
        for ch in a:
            if ch.isalnum() or ch in allowed_extra:
                continue
            raise ValidationError("Heimilisfang má bara innihalda bókstafi, tölur, bil og '-', ',' eða '.'.")
        return a
    
    def _normalize_phone(self, phone: str) -> str:
        digits = "".join(ch for ch in phone if ch.isdigit())
        if len(digits) != 7:
            raise ValidationError("Símanúmer verður að vera 7 tölustafir.")
        return "+354" + digits
    
    def _validate_email(self, email: str) -> str:
        e = email.strip()
        if not e:
            raise ValidationError("Þú verður að skrá netfang.")
        lower = e.lower()
        if "@" not in e or not (lower.endswith(".com") or lower.endswith(".is")):
            raise ValidationError("Netfang verður að innihalda '@' og enda á .com eða .is.")
        return e
    
    def _validate_handle_format(self, handle: str) -> str:
        h = handle.strip()
        if len(h) < 2:
            raise ValidationError("Leikmanna nafn (handle) verður að vera a.m.k. 2 stafir.")
        if len(h) > 30:
            raise ValidationError("Leikmanna nafn (handle) má ekki vera lengra en 30 stafir.")
        if h.startswith("/"):
            raise ValidationError("Leikmanna nafn (handle) má ekki byrja á '/'.")
        if " " in h:
            raise ValidationError("Leikmanna nafn (handle) má ekki innihalda bil.")
        if not any(ch.isalpha() for ch in h):
            raise ValidationError("Leikmanna nafn (handle) verður að innihalda a.m.k. einn bókstaf.")
        return h
    
    def _normalize_player_link(self, link: str) -> str:
        l = link.strip()
        if not l:
            return ""
        lower = l.lower()
        if not (lower.endswith(".com") or lower.endswith(".is") or lower.endswith(".tv")):
            raise ValidationError("Vefslóðin verður að enda á .is, .com eða .tv.")
        if not (lower.startswith("http://") or lower.startswith("https://")):
            l = "https://" + l
        return l

        
    
    