from datetime import date
from datetime import MAXYEAR
from datetime import MINYEAR
import math

MAX_TITLE = 38
MAX_ASTR = "*********************************************************"
MAX_SPACE =  "                                                        *"

class Event:
    """Event consisting of a title and date"""

    def __init__(self, eventName: str = "Default Event", eventDate:date = date(1900, 6, 9)):
        self.eventName = eventName
        self.eventDate = eventDate

    def print_event(self):
            print()
            self.print_header()
            self.print_next_occurrence()
            self.print_elapsed_years()
            self.print_elapsed_days()
            print(f"{MAX_ASTR}**")
            
    def print_header(self):
        """print event title and date"""
        # Date Width: 10, Whitespace Width: 5, Title Width: variable

        # fieldWidth = dateWidth + whiteWidth + titleWidth
        # totalEdgeWidth = maxWidth - fieldWidth
        # edgeWidth = totalEdgeWidth / 2
        # if (edgeWidth1 + edgeWidth2 + fieldWidth) < MAX_WIDTH
        #   edgeWidth2 +=1 

        field = f" {self.eventName} - {self.eventDate} "
        totalEdgeLen = MAX_ASTR.__len__() - field.__len__()
        edgeLen = int(totalEdgeLen / 2)

        edge1, edge2 = MAX_ASTR[:edgeLen], MAX_ASTR[:edgeLen]

        if((edge1.__len__() + edge2.__len__() + field.__len__()) < MAX_ASTR.__len__()):
            edge2 = MAX_ASTR[:edgeLen + 1]

        print(edge1, field, edge2)

    def print_elapsed_days(self):
        """print the days elapsed between the event and today"""

        # calculate
        elapsedDays = date.today() - self.eventDate
        field = f"* {elapsedDays.days} total day(s) since {self.eventDate}"

        # print results
        totalEdgeLen = MAX_SPACE.__len__() - field.__len__()
        edge = MAX_SPACE[-totalEdgeLen - 1:]
        print(field, edge)

    def print_elapsed_years(self):
        """print the years elapsed between the event and today"""

        # calculate
        elapsedDays = date.today() - self.eventDate
        elapsedYears = elapsedDays.days / 365
        remainder = elapsedDays.days % 365
        field = f"* {math.floor(elapsedYears)} year(s) since {self.eventDate} "

        # print results
        if(remainder > 0):
            field = f"* {math.floor(elapsedYears)} year(s) and {remainder} day(s) since {self.eventDate}"
        

        totalEdgeLen = MAX_SPACE.__len__() - field.__len__()
        edge = MAX_SPACE[-totalEdgeLen - 1:]
        print(field, edge)

    def print_next_occurrence(self):
        """print the date of next occurrence and days until then"""
        futureDate = date(date.today().year, self.eventDate.month, self.eventDate.day)
        daysUntil = futureDate - date.today()
        field = f"* Next Occurrence: {futureDate}, in {daysUntil.days} day(s) "

        #if event has already occurred this year then it happens next year
        if(daysUntil.days < 0):
            nextYear = date.today().year + 1
            futureDate = date(nextYear, self.eventDate.month, self.eventDate.day)
            daysUntil = futureDate - date.today()
            field = f"* Next Occurrence: {futureDate}, in {daysUntil.days} day(s) "
        elif(daysUntil.days == 0):
            field = f"* Next Occurrence: Today!!! "

        #print results
        totalEdgeLen = MAX_SPACE.__len__() - field.__len__()
        edge = MAX_SPACE[-totalEdgeLen - 1:]
        print(field, edge)


    def check_year(self, yearStr: str) -> bool:
        """checks if provided year is an integer in valid range"""
        try:
            year = int(yearStr)
        except:
            return False
        
        if(year < MINYEAR or year > MAXYEAR):
            return False
        else:
            return True

    def check_month(self, monthStr: str) -> bool:
        """checks if provided month is an integer in valid range"""

        try:
            month = int(monthStr)
        except:
            return False
        
        if(month < 1 or month > 12):
            return False
        else:
            return True

    def check_day(self, dayStr: str) -> bool:
        """only checks if provided day is an integer"""
        try:
            day = int(dayStr)
        except:
            return False
        
        if(day <= 0 or day > 31):
            return False
        else:
            return True

    def check_date(self, year: int, month: int, day: int) -> bool:
        """Checks date validity. Functionally it just checks if the 
            provided days is within range for the given year/month"""
        try:
            eventDate = date(year, month, day)
            return True
        except:
            return False

    def check_title(self, title: str) -> bool:
        """Checks if the given title is greater than 38 characters"""
        if(title.__len__() > MAX_TITLE or title.__len__() <= 0):
            return False

        return True
#---------- End Event Class ----------#
