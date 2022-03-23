from email.policy import default
import os
from sqlalchemy import (
    Column, 
    Integer, 
    Float,
    String, 
    ForeignKey,
    DateTime,
    create_engine
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from utilities.produce_folder import make_folder
from config import Folders


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name_first = Column(String(30))
    name_last = Column(String)
    username = Column(String)
    datetime = Column(DateTime, default=datetime.now())

    send = relationship("EmojiSend", back_populates='users')
    user_friend = relationship("Friend", back_populates='friend')
    user_emoji = relationship('UserEmoji', back_populates='users')
    notification = relationship('UserNotification', back_populates='users')

class Friend(Base):
    __tablename__ = 'friends'
    id = Column(Integer, primary_key=True)
    id_telegram = Column(Integer, ForeignKey('users.id'))
    name_friend = Column(String(100), default='Unknown Friend')
    friend = relationship('User', back_populates='user_friend')

class UserNotification(Base):
    __tablename__ = 'user_notifications'
    id_user = Column(Integer, ForeignKey('users.id'), primary_key=True)
    id_user_notification = Column(Integer)#, ForeignKey('users.id'), primary_key=True)

    users = relationship('User', back_populates='notification')

class Emoji(Base):
    __tablename__ = 'emojis'

    id = Column(Integer, primary_key=True)
    emo = Column(String(20))
    emo_value = Column(Float, default=1.0)

    send = relationship("EmojiSend", back_populates="emojis")
    user_emoji = relationship('UserEmoji', back_populates='emojis')

class UserEmoji(Base):
    __tablename__ = 'user_emojis'

    id_user = Column(Integer, ForeignKey('users.id'), primary_key=True)
    id_emoji = Column(Integer, ForeignKey('emojis.id'), primary_key=True)

    emojis = relationship('Emoji', back_populates='user_emoji')
    users = relationship("User", back_populates="user_emoji")

class EmojiSend(Base):
    __tablename__ = 'emojisend'
    id_user = Column(Integer, ForeignKey('users.id'), primary_key=True)
    id_user_friend = Column(Integer) #ForeignKey('users.id'), primary_key=True)
    id_emoji = Column(Integer, ForeignKey('emojis.id'), primary_key=True)
    
    users = relationship("User", back_populates="send")
    # users_friend = relationship("User", back_populates="send_friend")
    emojis = relationship("Emoji", back_populates="send")


path_folder = os.path.join(Folders.folder_here, Folders.folder_storage)
make_folder(path_folder)

engine = create_engine(f'sqlite:///{os.path.join(path_folder, Folders.db)}')
Base.metadata.create_all(engine)