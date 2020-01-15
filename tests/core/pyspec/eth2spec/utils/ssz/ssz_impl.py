from remerkleable.core import View
from remerkleable.tree import merkle_hash


def serialize(obj: View) -> bytes:
    return obj.encode_bytes()


def hash_tree_root(obj: View) -> bytes:
    return obj.get_backing().merkle_root(merkle_hash)
