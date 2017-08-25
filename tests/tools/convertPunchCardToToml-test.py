from tools import convertPunchCardToToml
import unittest


class parseDayTests(unittest.TestCase):

    def test_returnsWeekdayAndArrayOfPunches_givenWeekDayWithListOfPunches(self):
        weekDay = "M,8:00,12:00,12:30,5:00"
        actualOutput = convertPunchCardToToml.parseDay(weekDay, False)
        expectedOutput = ("monday", "'000' = ['8:00', '12:00', '12:30', '5:00']\n")
        self.assertEqual(actualOutput, expectedOutput)

    def test_returnsWeekdayAndNone_givenWeekDayWithJustLetter(self):
        weekDay = "T"
        actualOutput = convertPunchCardToToml.parseDay(weekDay, False)
        expectedOutput = ("tuesday", None)
        self.assertEqual(actualOutput, expectedOutput)

    def test_returnsWeekdayAndArrayOfPunchesForSunday_givenWeekDayWithListOfPunchesAndSundayFlagTrue(self):
        weekDay = "S,8:00,12:00,12:30,5:00"
        actualOutput = convertPunchCardToToml.parseDay(weekDay, True)
        expectedOutput = ("sunday", "'000' = ['8:00', '12:00', '12:30', '5:00']\n")
        self.assertEqual(actualOutput, expectedOutput)


class mainTests(unittest.TestCase):

    def test_returnsTomlPunchCardWithZeroPunches_givenOldPunchCardWithZeroPunches(self):
        oldPunchCard = [
            'Week ending on 12/9/16',
            'S',
            'S',
            'M',
            'T',
            'W',
            'R',
            'F'
            ]
        expectedOutput = (
            "title = 'Week ending on 12/9/16'"
            "\n\n[day]"
            "\n\n  projects = ['000']"
            "\n\n  [day.saturday]"
            "\n    \n  [day.sunday]"
            "\n    \n  [day.monday]"
            "\n    \n  [day.tuesday]"
            "\n    \n  [day.wednesday]"
            "\n    \n  [day.thursday]"
            "\n    \n  [day.friday]"
            "\n    \n"
        )
        actualOutput = convertPunchCardToToml.main(oldPunchCard)
        self.assertEqual(actualOutput, expectedOutput)

    def test_returnsTomlPunchCardWithPunches_givenOldPunchCardWithPunches(self):
        oldPunchCard = [
            'Week ending on 12/9/16',
            'S',
            'S',
            'M,8:10,12:00,12:30,5:10',
            'T,8:10,10:00,10:10,12:10,12:40,2:00,2:10,5:00',
            'W',
            'R,8:00,4:00',
            'F,8:00,8:00'
            ]
        expectedOutput = (
            "title = 'Week ending on 12/9/16'"
            "\n\n[day]"
            "\n\n  projects = ['000']"
            "\n\n  [day.saturday]"
            "\n    \n  [day.sunday]"
            "\n    \n  [day.monday]"
            "\n    '000' = ['8:10', '12:00', '12:30', '5:10']"
            "\n\n  [day.tuesday]"
            "\n    '000' = ['8:10', '10:00', '10:10', '12:10', '12:40', '2:00', '2:10', '5:00']"
            "\n\n  [day.wednesday]"
            "\n    \n  [day.thursday]"
            "\n    '000' = ['8:00', '4:00']"
            "\n\n  [day.friday]"
            "\n    '000' = ['8:00', '8:00']\n\n"
        )
        actualOutput = convertPunchCardToToml.main(oldPunchCard)
        self.assertEqual(actualOutput, expectedOutput)


if __name__ == '__main__':
    unittest.main()
