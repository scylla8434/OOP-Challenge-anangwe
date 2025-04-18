# pet.py

class Pet:
    """A unique, personality‑packed virtual companion."""

    MAX_STAT = 10
    MIN_STAT = 0

    def __init__(self, name: str):
        self.name = name
        # Start in the balanced “just right” zone
        self.hunger = 5      
        self.energy = 5      
        self.happiness = 5   
        self.tricks = []     
        print(f"🎉 Meet {self.name}, your fabulous new Pet! 🎉\n")

    def _clamp(self, value: int) -> int:
        """Ensure stats stay within [0, 10]."""
        return max(self.MIN_STAT, min(self.MAX_STAT, value))

    def eat(self):
        """Feed: −3 hunger, +1 happiness."""
        before_h, before_hp = self.hunger, self.happiness
        self.hunger = self._clamp(self.hunger - 3)
        self.happiness = self._clamp(self.happiness + 1)
        print(
            f"🍽️  {self.name} feasts! "
            f"Hunger: {before_h}→{self.hunger}, "
            f"Happiness: {before_hp}→{self.happiness}"
        )

    def sleep(self):
        """Rest: +5 energy."""
        before = self.energy
        self.energy = self._clamp(self.energy + 5)
        print(f"🛏️  {self.name} sleeps soundly! Energy: {before}→{self.energy}")

    def play(self):
        """Play: −2 energy, +2 happiness, +1 hunger."""
        if self.energy < 2:
            print(f"😴  {self.name} is too tired to play right now.")
            return
        b_e, b_h, b_hg = self.energy, self.happiness, self.hunger
        self.energy = self._clamp(self.energy - 2)
        self.happiness = self._clamp(self.happiness + 2)
        self.hunger = self._clamp(self.hunger + 1)
        print(
            f"🎾  {self.name} plays joyfully! "
            f"Energy: {b_e}→{self.energy}, "
            f"Happiness: {b_h}→{self.happiness}, "
            f"Hunger: {b_hg}→{self.hunger}"
        )

    def get_status(self):
        """Display a clear, bar‑style snapshot of all stats."""
        bar = lambda v: '■' * v + '·' * (self.MAX_STAT - v)
        print("\n🔍  Current Status:")
        print(f"  Name     : {self.name}")
        print(f"  Hunger   : {bar(self.hunger)} {self.hunger}/{self.MAX_STAT}")
        print(f"  Energy   : {bar(self.energy)} {self.energy}/{self.MAX_STAT}")
        print(f"  Happiness: {bar(self.happiness)} {self.happiness}/{self.MAX_STAT}")
        print("")

    # — Bonus Features —
    def train(self, trick: str):
        """Teach a new trick if not already known."""
        normalized = trick.lower()
        known = [t.lower() for t in self.tricks]
        if normalized in known:
            print(f"😉  {self.name} already knows “{trick}.”")
        else:
            self.tricks.append(trick)
            print(f"🏅  {self.name} mastered “{trick}!”")

    def show_tricks(self):
        """List all learned tricks, or a friendly nudge if none."""
        if not self.tricks:
            print(f"🤷  {self.name} hasn't learned any tricks yet.")
        else:
            print(f"✨  {self.name}'s Tricks: " + ", ".join(f"“{t}”" for t in self.tricks))
