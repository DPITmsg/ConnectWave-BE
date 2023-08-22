from backend.repository.UserRepository import UserRepository


def init_db():
    UserRepository.create("Pop")
