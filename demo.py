# from us_visa.logger import logging
# from us_visa.exception import USvisaException
# logging.info("Welcome to our custom log")
# import sys
# try:
#     a=2/0
# except Exception as e:
#     raise USvisaException(e,sys)

# import os
# mongo_db_url = os.getenv('MONGODB_URL')
# print(mongo_db_url)


from us_visa.pipline.training_pipeline import TrainPipeline

obj=TrainPipeline()
obj.run_pipeline()

