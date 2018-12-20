import os


API_SPECS_PATH: str = os.environ.get('API_SPECS_PATH', 'docs/api/v1/openapi.yaml')
LOG_LEVEL: str = os.environ.get('LOG_LEVEL', 'INFO')

JWT_ISSUER: str = os.environ.get('JWT_ISSUER', 'aiolambda')
JWT_SECRET: str = os.environ.get('JWT_SECRET', 'test1234')
JWT_LIFETIME_SECONDS: int = int(os.environ.get('JWT_LIFETIME_SECONDS', 600))
JWT_ALGORITHM: str = os.environ.get('JWT_ALGORITHM', 'HS256')

POSTGRES_HOST: str = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_PORT: int = int(os.environ.get('POSTGRES_PORT', '5432'))
POSTGRES_DB: str = os.environ.get('POSTGRES_DB', 'test')
POSTGRES_USER: str = os.environ.get('POSTGRES_USER', 'test')
POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD', 'test1234')

RABBIT_HOST: str = os.environ.get('RABBIT_HOST', 'localhost')
RABBIT_USER: str = os.environ.get('RABBIT_USER', 'test')
RABBIT_PASSWORD: str = os.environ.get('RABBIT_PASSWORD', 'test1234')
