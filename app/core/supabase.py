from functools import lru_cache

from supabase import Client, create_client

from app.core.config import settings


@lru_cache
def get_supabase_client() -> Client:
    client: Client = create_client(
        settings.supabase_url,
        settings.supabase_secret_key,
    )

    return client


supabase: Client = get_supabase_client()