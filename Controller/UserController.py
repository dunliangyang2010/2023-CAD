from sqlalchemy.orm import Session
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Model import Database, Models

def get_user(db: Session, user_id: int):
    return db.query(Models.User).filter(Models.User.id == user_id).first()

if __name__=="__main__":
    se = Database.UserBase()
    user = get_user(se.session(), 1)

    if user:
        # print(f"User found: {user.name}, ID: {user.id}")
        print(f"User found: {user.name}")
    else:
        print("User not found.")