from dataclasses import dataclass, field

from browserforge.fingerprints import Fingerprint


@dataclass
class Proxy:
    server: str | None = None
    port: int | None = None
    username: str | None = None
    password: str | None = None


@dataclass
class Profile:
    fingerprint: Fingerprint
    proxy: Proxy | None = None
    page_urls: list[str] = field(default_factory=list)
