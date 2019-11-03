import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). 
    while True:
        city=input("Select city to analize from \n...(chicago, new york city, washington)  : ").lower()
        if city in ('chicago', 'new york city', 'washington'):
            break
        else: print("\n Wrong city name \n") 
    

    # get user input for month (all, january, february, ... , june)
    while True:
        month=input("input month month\n...(All,January, February, March, April, May, June) : ").lower().title()
        if month in ('All','January', 'February', 'March', 'April', 'May', 'June'):
            break
        else: print("\n Wrong month name \n") 

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("input Day of week\n...('All','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') : ").lower().title()
        if day in ('All','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
            break
        else: print("\n Wrong day name \n") 
    print("\n you select {} city, {} month, {} as day of week".format(city,month,day)) #print the selection be for calculating
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month_name']=pd.to_datetime(df['Start Time']).dt.month_name()
    df['day_name']=df['Start Time'].dt.weekday_name
    if month!='All':
        df= df[df['month_name'] == month]
    if day!= 'All':
        df=df[df['day_name'] == day]

    return df

def checkEmpity(city, month, day):
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month_name']=pd.to_datetime(df['Start Time']).dt.month_name()
    df['day_name']=df['Start Time'].dt.weekday_name
    if month!='All':
        df= df[df['month_name'] == month]
    if day!= 'All':
        df=df[df['day_name'] == day]



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print ('The most common month is : {}'.format(df['month_name'].value_counts().idxmax()))

    # display the most common day of week
    print ('The most common day of week is : {}'.format(df['day_name'].value_counts().idxmax()))

    # display the most common start hour
    print ('The most common start hour is : {}'.format(df['Start Time'].dt.hour.value_counts().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station')
    print(df['Start Station'].value_counts().idxmax())

    # display most commonly used end station
    print('\nThe most commonly used end station')
    print(df['End Station'].value_counts().idxmax())

    # display most frequent combination of start station and end station trip
    print('\nThe most frequent combination of start station and end station trip ')
    print(df.groupby(['Start Station','End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\nTotal travel time is : '+ str(df['Trip Duration'].sum()))


    # display mean travel time
    print('Mean travel time is : '+ str(df['Trip Duration'].mean()))



    print("This took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nCounts of user types :')
    print(df['User Type'].value_counts())

    # Display counts of gender
    print('\nCounts of gender :')
    
    print(df['Gender'].value_counts())
    


    # Display earliest, most recent, and most common year of birth
    myear=int(df['Birth Year'].min())
    maxyear=int(df['Birth Year'].max())
    comyear=int(df['Birth Year'].value_counts().idxmax())
    text= "\n\nThe earliest year of birth is {}\nThe most recent year of birth is {}\nThe most common year of birth is {}"
    print(text.format(myear,maxyear,comyear))   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def showRowData(df):

    """"
    Displays five lines of data depend on user input that they would like to.
    then ask the user if they would like to see five more, continuing asking until they say stop.  

    INPUT: DataFrame
    """
    isshow=input('\nWould you like to see a five lines of the row data? Enter yes or no.\n')
    if isshow == 'yes':
        i=0
        #lastRow=df.index.stop                #in pandas.__version__="0.25.2"
        lastRow=df.shape[0]                   #in pandas.__version__="0.23.3"
        while True:
            table=df.iloc[i:i+5,:-2]
            print(table)
            iscontinue=input('\nWould you like to see a more five lines?\npress "Enter" to show more or type "stop" to containue the program : ')
            if iscontinue == 'stop' :
                break
            if  i >= lastRow - 6:
                print(df.iloc[i:lastRow,:-2])
                print('\n\nThat is the last lines')
                break
            i+=5





def main():
    
    while True:
        city, month, day = get_filters()
        try:    
            df = load_data(city, month, day)
        except :
            print("There is no data for your filteration values\ntry other values") 

        showRowData(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)

        try:
            user_stats(df)
        except(KeyError):
            print('\nThere is no Gender Column in {} city table'.format(city))

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
