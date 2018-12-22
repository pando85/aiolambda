import os


DEFAULT_PRIVATE_KEY = """-----BEGIN RSA PRIVATE KEY-----
MIICWwIBAAKBgQDdlatRjRjogo3WojgGHFHYLugdUWAY9iR3fy4arWNA1KoS8kVw
33cJibXr8bvwUAUparCwlvdbH6dvEOfou0/gCFQsHUfQrSDv+MuSUMAe8jzKE4qW
+jK+xQU9a03GUnKHkkle+Q0pX/g6jXZ7r1/xAK5Do2kQ+X5xK9cipRgEKwIDAQAB
AoGAD+onAtVye4ic7VR7V50DF9bOnwRwNXrARcDhq9LWNRrRGElESYYTQ6EbatXS
3MCyjjX2eMhu/aF5YhXBwkppwxg+EOmXeh+MzL7Zh284OuPbkglAaGhV9bb6/5Cp
uGb1esyPbYW+Ty2PC0GSZfIXkXs76jXAu9TOBvD0ybc2YlkCQQDywg2R/7t3Q2OE
2+yo382CLJdrlSLVROWKwb4tb2PjhY4XAwV8d1vy0RenxTB+K5Mu57uVSTHtrMK0
GAtFr833AkEA6avx20OHo61Yela/4k5kQDtjEf1N0LfI+BcWZtxsS3jDM3i1Hp0K
Su5rsCPb8acJo5RO26gGVrfAsDcIXKC+bQJAZZ2XIpsitLyPpuiMOvBbzPavd4gY
6Z8KWrfYzJoI/Q9FuBo6rKwl4BFoToD7WIUS+hpkagwWiz+6zLoX1dbOZwJACmH5
fSSjAkLRi54PKJ8TFUeOP15h9sQzydI8zJU+upvDEKZsZc/UhT/SySDOxQ4G/523
Y0sz/OZtSWcol/UMgQJALesy++GdvoIDLfJX5GBQpuFgFenRiRDabxrE9MNUZ2aP
FaFp+DyAe+b4nDwuJaW2LURbr8AEZga7oQj0uYxcYw==
-----END RSA PRIVATE KEY-----"""

DEFAULT_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDdlatRjRjogo3WojgGHFHYLugd
UWAY9iR3fy4arWNA1KoS8kVw33cJibXr8bvwUAUparCwlvdbH6dvEOfou0/gCFQs
HUfQrSDv+MuSUMAe8jzKE4qW+jK+xQU9a03GUnKHkkle+Q0pX/g6jXZ7r1/xAK5D
o2kQ+X5xK9cipRgEKwIDAQAB
-----END PUBLIC KEY-----"""

API_SPECS_PATH: str = os.environ.get('API_SPECS_PATH', 'docs/api/v1/openapi.yaml')
LOG_LEVEL: str = os.environ.get('LOG_LEVEL', 'INFO')

JWT_ISSUER: str = os.environ.get('JWT_ISSUER', 'aiolambda')
JWT_PRIVATE_KEY: str = os.environ.get('JWT_PRIVATE_KEY', DEFAULT_PRIVATE_KEY)
JWT_PUBLIC_KEY: str = os.environ.get('JWT_PUBLIC_KEY', DEFAULT_PUBLIC_KEY)
JWT_LIFETIME_SECONDS: int = int(os.environ.get('JWT_LIFETIME_SECONDS', 600))
JWT_ALGORITHM: str = os.environ.get('JWT_ALGORITHM', 'RS256')

POSTGRES_HOST: str = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_PORT: int = int(os.environ.get('POSTGRES_PORT', '5432'))
POSTGRES_DB: str = os.environ.get('POSTGRES_DB', 'test')
POSTGRES_USER: str = os.environ.get('POSTGRES_USER', 'test')
POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD', 'test1234')

RABBIT_HOST: str = os.environ.get('RABBIT_HOST', 'localhost')
RABBIT_USER: str = os.environ.get('RABBIT_USER', 'test')
RABBIT_PASSWORD: str = os.environ.get('RABBIT_PASSWORD', 'test1234')
