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

    def test_returnsZeroAndEmptyErrorString_givenEmptyArray(self):
        self.assertEqual(PunchCard.calculateDay([]), (0.0, ''))

    def test_returnsZeroAndEmptyErrorString_givenTwoEqualTimeEntries(self):
        self.assertEqual(PunchCard.calculateDay(['8:00', '8:00']), (0.0, ''))

    def test_returnsEightAndEmptyErrorString_givenFourEntries(self):
        dayEntry = ['8:00', '12:00', '1:00', '5:00']
        self.assertEqual(PunchCard.calculateDay(dayEntry), (8.0, ''))

    def test_returnsEightAndEmptyErrorString_givenTwoEntries(self):
        self.assertEqual(PunchCard.calculateDay(['8:00', '4:00']), (8.0, ''))

    def test_returnsEightHoursTenMinutesAsDecimalAndEmptyErrorString_givenTwoEntries(self):
        self.assertEqual(PunchCard.calculateDay(['8:00', '4:10']), (8.166666666666666, ''))

    def test_returnsZeroAndOneInvalidTimeError_givenAnIncorrectFirstTime(self):
        self.assertEqual(PunchCard.calculateDay(['a', '10:00']), (0, '\nInvalid time: a'))

    def test_returnsZeroAndOneInvalidTimeError_givenAnIncorrectSecondTime(self):
        self.assertEqual(PunchCard.calculateDay(['8:00', '10:$0']), (0, '\nInvalid time: 10:$0'))

    def test_returnsZeroAndTwoInvalidTimeError_givenTwoIncorrectTimes(self):
        self.assertEqual(PunchCard.calculateDay(['a', '10:$0']), (0, '\nInvalid time: a\nInvalid time: 10:$0'))


class PrintDaysHoursTests(unittest.TestCase):

    def test_returnsStringForDayWithHoursMinutesAndDecimalHours_givenNoTimeFormat(self):
        actualOutput = PunchCard.printDaysHours('monday', 8.166666666666666, None)
        expectedOutput = '\nMonday: 8 hours 10 minutes(8.167 hours)'
        self.assertEqual(actualOutput, expectedOutput)

    def test_returnsStringForDayWithHoursMinutesAndDecimalHours_givenAnyStringAsATimeFormat(self):
        actualOutput = PunchCard.printDaysHours('monday', 8.166666666666666, 'aaa')
        expectedOutput = '\nMonday: 8 hours 10 minutes(8.167 hours)'
        self.assertEqual(actualOutput, expectedOutput)

    def test_returnsStringForDayWithHoursMinutesAndDecimalHours_givenAnyNumberAsATimeFormat(self):
        actualOutput = PunchCard.printDaysHours('monday', 8.166666666666666, 6.6)
        expectedOutput = '\nMonday: 8 hours 10 minutes(8.167 hours)'
        self.assertEqual(actualOutput, expectedOutput)

    def test_returnsStringForDayWithHoursMinutes_givenTimeFormatHHmm(self):
        actualOutput = PunchCard.printDaysHours('monday', 8.166666666666666, 'HH:mm')
        expectedOutput = '\nMonday: 8 hours 10 minutes'
        self.assertEqual(actualOutput, expectedOutput)

    def test_returnsStringForDayWithDecimalHours_givenTimeFormatHHhhh(self):
        actualOutput = PunchCard.printDaysHours('monday', 8.166666666666666, 'HH.hhh')
        expectedOutput = '\nMonday: 8.167 hours'
        self.assertEqual(actualOutput, expectedOutput)

    def test_throwsError_givenAStringForHours(self):
        with self.assertRaises(TypeError):
            PunchCard.printDaysHours('monday', 'a', 'HH.hhh')


class PrintWeekHoursTests(unittest.TestCase):

    def test_returnsStringForWeekWithHoursMinutesAndDecimalHours_givenNoTimeFormat(self):
        actualOutput = PunchCard.printWeekHours(8.166666666666666, None)
        expectedOutput = '\nTotal hours for the week: 8 hours 10 minutes(8.167 hours)'
        self.assertEqual(actualOutput, expectedOutput)

    def test_returnsStringForWeekWithHoursMinutesAndDecimalHours_givenAnyStringAsATimeFormat(self):
        actualOutput = PunchCard.printWeekHours(8.166666666666666, 'aaa')
        expectedOutput = '\nTotal hours for the week: 8 hours 10 minutes(8.167 hours)'
        self.assertEqual(actualOutput, expectedOutput)

    def test_returnsStringForWeekWithHoursMinutesAndDecimalHours_givenAnyNumberAsATimeFormat(self):
        actualOutput = PunchCard.printWeekHours(8.166666666666666, 6.6)
        expectedOutput = '\nTotal hours for the week: 8 hours 10 minutes(8.167 hours)'
        self.assertEqual(actualOutput, expectedOutput)

    def test_returnsStringForWeekWithHoursMinutes_givenTimeFormatHHmm(self):
        actualOutput = PunchCard.printWeekHours(8.166666666666666, 'HH:mm')
        expectedOutput = '\nTotal hours for the week: 8 hours 10 minutes'
        self.assertEqual(actualOutput, expectedOutput)

    def test_returnsStringForWeekWithDecimalHours_givenTimeFormatHHhhh(self):
        actualOutput = PunchCard.printWeekHours(8.166666666666666, 'HH.hhh')
        expectedOutput = '\nTotal hours for the week: 8.167 hours'
        self.assertEqual(actualOutput, expectedOutput)

    def test_throwsError_givenAStringForHours(self):
        with self.assertRaises(TypeError):
            PunchCard.printWeekHours('a', 'HH.hhh')


class ValidDayTests(unittest.TestCase):
    def test_returnsTrue_givenEvenNumberOfTimePunches(self):
        self.assertTrue(PunchCard.validDay(['8:00', '12:00', '12:30', '4:00']))

    def test_returnsTrue_givenZeroTimePunches(self):
        self.assertTrue(PunchCard.validDay([]))

    def test_returnsFalse_givenOddNumberOfTimePunches(self):
        self.assertFalse(PunchCard.validDay(['8:00', '12:00', '12:30']))


class ValidTimeTests(unittest.TestCase):
    def test_returnsTrue_givenValid24HourTime(self):
        self.assertTrue(PunchCard.validTime('17:00'))

    def test_returnsTrue_givenValid12HourTime(self):
        self.assertTrue(PunchCard.validTime('5:00'))

    def test_returnsFalse_givenATimeWithHoursOver24(self):
        self.assertFalse(PunchCard.validTime('48:00'))

    def test_returnsFalse_givenATimeWithMinutesOver59(self):
        self.assertFalse(PunchCard.validTime('12:76'))

    def test_returnsFalse_givenNonNumbers(self):
        self.assertFalse(PunchCard.validTime('a:b'))

    def test_returnsFalse_givenNoNumbers(self):
        self.assertFalse(PunchCard.validTime(':'))

    def test_returnsFalse_givenEmptyString(self):
        self.assertFalse(PunchCard.validTime(''))

    def test_returnsFalse_givenNone(self):
        self.assertFalse(PunchCard.validTime(None))


if __name__ == '__main__':
    unittest.main()
