import os
import PunchCard
import sys
import unittest

sys.path.insert(0, os.path.abspath('..'))


class CaclWorkTimeTests(unittest.TestCase):

    def test_returnsTwo_givenEightAndTenOclock(self):
        self.assertEqual(PunchCard.calcWorkTime('8:00', '10:00'), 2)

    def test_returnsZero_givenEightAndEightOclock(self):
        self.assertEqual(PunchCard.calcWorkTime('8:00', '8:00'), 0)

    def test_returnsFour_givenTenAndTwoOclock(self):
        self.assertEqual(PunchCard.calcWorkTime('10:00', '2:00'), 4)

    def test_returnsTwoAndHalf_givenEightThirtyAndElevenOclock(self):
        self.assertEqual(PunchCard.calcWorkTime('8:30', '11:00'), 2.5)

    def test_throwsError_givenAnIncorrectTime(self):
        with self.assertRaises(ValueError):
            PunchCard.calcWorkTime('a', '10:00')


class CalculateDayTests(unittest.TestCase):

    def test_returnsZero_givenEmptyArray(self):
        self.assertEqual(PunchCard.calculateDay([]), 0.0)

    def test_returnsZero_givenTwoEqualTimeEntries(self):
        self.assertEqual(PunchCard.calculateDay(['8:00', '8:00']), 0.0)

    def test_returnsEight_givenFourEntries(self):
        dayEntry = ['8:00', '12:00', '1:00', '5:00']
        self.assertEqual(PunchCard.calculateDay(dayEntry), 8.0)

    def test_returnsEight_givenTwoEntries(self):
        self.assertEqual(PunchCard.calculateDay(['8:00', '4:00']), 8.0)

    def test_returnsEightHoursTenMinutesAsDecimal_givenTwoEntries(self):
        self.assertEqual(PunchCard.calculateDay(['8:00', '4:10']), 8.166666666666666)

    def test_throwsError_givenAnIncorrectTime(self):
        with self.assertRaises(ValueError):
            PunchCard.calculateDay(['a', '10:00'])


class PrintDaysHoursTests(unittest.TestCase):

    def test_printsStringForDayWithHoursMinutesAndDecimalHours_givenNoTimeFormat(self):
        PunchCard.printDaysHours('M', 8.166666666666666, None)
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        actualOutput = sys.stdout.getvalue().strip()
        expectedOutput = 'M: 8 hours 10 minutes(8.167 hours)'
        self.assertEqual(actualOutput, expectedOutput)

    def test_printsStringForDayWithHoursMinutesAndDecimalHours_givenAnyStringAsATimeFormat(self):
        PunchCard.printDaysHours('M', 8.166666666666666, 'aaa')
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        actualOutput = sys.stdout.getvalue().strip()
        expectedOutput = 'M: 8 hours 10 minutes(8.167 hours)'
        self.assertEqual(actualOutput, expectedOutput)

    def test_printsStringForDayWithHoursMinutesAndDecimalHours_givenAnyNumberAsATimeFormat(self):
        PunchCard.printDaysHours('M', 8.166666666666666, 6.6)
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        actualOutput = sys.stdout.getvalue().strip()
        expectedOutput = 'M: 8 hours 10 minutes(8.167 hours)'
        self.assertEqual(actualOutput, expectedOutput)

    def test_printsStringForDayWithHoursMinutes_givenTimeFormatHHmm(self):
        PunchCard.printDaysHours('M', 8.166666666666666, 'HH:mm')
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        actualOutput = sys.stdout.getvalue().strip()
        expectedOutput = 'M: 8 hours 10 minutes'
        self.assertEqual(actualOutput, expectedOutput)

    def test_printsStringForDayWithDecimalHours_givenTimeFormatHHhhh(self):
        PunchCard.printDaysHours('M', 8.166666666666666, 'HH.hhh')
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        actualOutput = sys.stdout.getvalue().strip()
        expectedOutput = 'M: 8.167 hours'
        self.assertEqual(actualOutput, expectedOutput)

    def test_throwsError_givenAStringForHours(self):
        with self.assertRaises(TypeError):
            PunchCard.printDaysHours('M', 'a', 'HH.hhh')


class PrintWeekHoursTests(unittest.TestCase):

    def test_printsStringForWeekWithHoursMinutesAndDecimalHours_givenNoTimeFormat(self):
        PunchCard.printWeekHours(8.166666666666666, None)
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        actualOutput = sys.stdout.getvalue().strip()
        expectedOutput = 'Total hours for the week: 8 hours 10 minutes(8.167 hours)'
        self.assertEqual(actualOutput, expectedOutput)

    def test_printsStringForWeekWithHoursMinutesAndDecimalHours_givenAnyStringAsATimeFormat(self):
        PunchCard.printWeekHours(8.166666666666666, 'aaa')
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        actualOutput = sys.stdout.getvalue().strip()
        expectedOutput = 'Total hours for the week: 8 hours 10 minutes(8.167 hours)'
        self.assertEqual(actualOutput, expectedOutput)

    def test_printsStringForWeekWithHoursMinutesAndDecimalHours_givenAnyNumberAsATimeFormat(self):
        PunchCard.printWeekHours(8.166666666666666, 6.6)
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        actualOutput = sys.stdout.getvalue().strip()
        expectedOutput = 'Total hours for the week: 8 hours 10 minutes(8.167 hours)'
        self.assertEqual(actualOutput, expectedOutput)

    def test_printsStringForWeekWithHoursMinutes_givenTimeFormatHHmm(self):
        PunchCard.printWeekHours(8.166666666666666, 'HH:mm')
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        actualOutput = sys.stdout.getvalue().strip()
        expectedOutput = 'Total hours for the week: 8 hours 10 minutes'
        self.assertEqual(actualOutput, expectedOutput)

    def test_printsStringForWeekWithDecimalHours_givenTimeFormatHHhhh(self):
        PunchCard.printWeekHours(8.166666666666666, 'HH.hhh')
        if not hasattr(sys.stdout, "getvalue"):
            self.fail("need to run in buffered mode")
        actualOutput = sys.stdout.getvalue().strip()
        expectedOutput = 'Total hours for the week: 8.167 hours'
        self.assertEqual(actualOutput, expectedOutput)

    def test_throwsError_givenAStringForHours(self):
        with self.assertRaises(TypeError):
            PunchCard.printWeekHours('a', 'HH.hhh')


if __name__ == '__main__':
    unittest.main()
