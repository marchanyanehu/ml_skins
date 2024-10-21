import os
import pandas as pd

def export_as_csv(model, session):
    # Get table name from the model
    table_name = model.__tablename__
    
    # Query all data from the table
    data = session.query(model).all()
    
    # Convert data to a list of dictionaries
    data_dicts = [row.__dict__ for row in data]
    
    # Remove SQLAlchemy internal state key
    for d in data_dicts:
        d.pop('_sa_instance_state', None)
    
    # Convert to DataFrame
    df = pd.DataFrame(data_dicts)
    
    # Define the export path
    export_path = os.path.join('csv_exports', f'{table_name}.csv')
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(export_path), exist_ok=True)
    
    # Save DataFrame to CSV
    df.to_csv(export_path, index=False)
    
    print(f"Data exported to {export_path}")

# Example usage:
# from your_model_file import YourModel
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy import create_engine
# 
# engine = create_engine('your_database_url')
# Session = sessionmaker(bind=engine)
# session = Session()
# 
# export_as_csv(YourModel, session)