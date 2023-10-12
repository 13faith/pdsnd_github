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
    print('Hi there! let\'s delve into some US bikeshare data')
    city = ''
    month = 'all' #initializing month to 'all'
    day = 'all' #initialize day
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    months = ['all','January','February', 'March', 'April', 'May', 'June']
    days = ['All', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    while True:
        city = input('Which one of these cities would you want to explore? \n Chicago, New York or Washington \n').lower()
        if city in cities:
            break
        else:
            print('Sorry, I can\'t help you with some bikeshare information in {}'.format(city))

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        filter = input('How would you like to filter the data? month, day, or none? \n').lower()
        if filter in ['month','day', 'none']:
            break
        else:
            print('invalid input. please enter "month," "day," or "none."')

        if filter == 'month':
            month = input('please enter the month you want to explore. \n You can enter \'all\', if you do not want to filter by month.\n Options: All, January, February, March, April, May, June \n').lower()
            if month not in months:
                print('enter a valid month.')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        elif filter == 'day':
            day = input('please enter the day of the week you want to explore. If you don\'t want to apply a weekly filter then enter \'all\'. \n Options: All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday \n').lower()
            month = 'all'
            if day in days:
                break
            else:
                print('Enter a valid day of the week')
        elif filter == 'none':
            month = 'all'
            day = 'all'
            break

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
    # retrieving data from a file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # transforming the 'Start Time' column into a datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create new columns by extracting the month and day of the week from the 'Start Time'
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month when applicable
    if month != 'all':
        # retrieve the corresponding integer using the index from the 'months' list
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # use the month as a filter to create a new dataframe
        df = df[df['month'] == month]

    # filter by day of week when applicable
    if day != 'all':
        # use day of week as filter to create a new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    if common_month == 1:
        common_month = 'January'
    elif common_month == 2:
        common_month = 'February'
    elif common_month == 3:
        common_month = 'March'
    elif common_month == 4:
        common_month = 'April'
    elif common_month == 5:
        common_month = 'May'
    elif common_month == 6:
        common_month = 'June'
    print('The most common month is {}'.format(common_month))

    # TO DO: display the most common day of week
    #df['day_of_week'] = df['Start Time'].dt.weekday_name
    most_common_weekday = df['day_of_week'].mode()[0]
    print('The most common day of the week is {}'.format(most_common_weekday))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    if most_common_hour < 12:
        print('The most common start hour is {} AM'.format(most_common_hour))
    else:
        print('The most common start hour is {} PM'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}'.format(most_used_start_station))

    # TO DO: display most commonly used end station
    most_used_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is {}'.format(most_used_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    combination_of_stations = df['Start Station'] + ' and ' + df['End Station']
    most_common_stations = combination_of_stations.mode()[0]
    print('Most frequent combination of start station and end station trip is {}'.format(most_common_stations))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration_of_trip = df['Trip Duration'].sum()
    print('The total travel time is {} seconds'.format(total_duration_of_trip))

    # TO DO: display mean travel time
    average_trip_duration = df['Trip Duration'].mean()
    print('The average travel time is {}'.format(average_trip_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User types: \n {}'.format(user_types))
    print('-'*40)




    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print('Count of user\'s gender: \n {}'.format(user_gender))
        print('-'*40)



    except:
        print('sorry! There\'s no gender data available for this City')

    print('-'*40)

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        most_early = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode())
        print('The most early user(s) birth year is {}'.format(most_early))
        print('The most recent user(s) birth year is {}'.format(most_recent))
        print('The most common user(s) birth year is {}'.format(most_common))
    except:
        print('sorry! There\'s no birth year data available for this City')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_data(df):
    ''' Prompts the users if they want to see lines of the raw data.'''
    start = 0
    stop = 5
    df_length = len(df)
    while start < df_length:
        view_data = input('Hey! Would you like to see lines of the raw data used in this analysis? Enter \'Yes\' or \'No\'').lower()
        if view_data == 'yes':
            print('Displaying only 5 lines of the data')
            if stop > df_length:
                stop = df_length
            print(df.iloc[start:stop])
            start += 5
            stop += 5
        else:
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        trip_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
