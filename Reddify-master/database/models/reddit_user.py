from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

from ..base import Base


class RedditUser(Base):

    __tablename__ = 'reddit_users'

    user_id = Column(String(10), primary_key=True)
    discord_user = Column(Integer, ForeignKey("discord_users.user_id"), nullable=False)
    discord_account = relationship("DiscordUser")
    username = Column(String(50), unique=True)
    verified = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Reddit User id='{self.user_id}' username='{self.username}'>"
