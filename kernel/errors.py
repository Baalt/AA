class SimilarCommandError(Exception):
    pass


class RunError(Exception):
    pass


class LiveScraperError(Exception):
    pass


class NotEnoughMatchError(LiveScraperError):
    pass


class MatchManagerError(Exception):
    pass


class ValidStructureError(Exception):
    pass
