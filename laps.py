"""Lap tracking for the stopwatch."""


class LapTracker:
    """Stores lap durations in milliseconds, in order."""

    def __init__(self):
        self._laps = []

    def add(self, ms):
        """Record one lap duration. Returns the new lap count."""
        self._laps.append(ms)
        return len(self._laps)

    def clear(self):
        """Forget all recorded laps."""
        self._laps.clear()

    def __len__(self):
        return len(self._laps)

    def __iter__(self):
        return iter(self._laps)

    @staticmethod
    def format(ms):
        """Format a duration in milliseconds as mm:ss:cc."""
        minutes    = ms // 60000
        seconds    = (ms // 1000) % 60
        hundredths = (ms % 1000) // 10
        return f"{minutes:02d}:{seconds:02d}:{hundredths:02d}"
