import datetime

class TimestampConverter:
    def epoch_to_datetime(self, epoch_time):
        # Convert epoch time to datetime object
        epoch_corrected = epoch_time/1000
        dt_object = datetime.datetime.fromtimestamp(epoch_corrected)
        
        # Format the datetime object as a string
        dt_string = dt_object.strftime("%Y-%m-%d %H:%M:%S")
        
        # Return the formatted string
        return dt_string
