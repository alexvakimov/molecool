"""
Unit test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import molecool
import numpy as np
import pytest
#import sys

def test_calculate_distance():
    """Test that calculate_distance function calculates what we expect"""

    r1 = np.array([1.0, 0.0, 0.0])
    r2 = np.array([0.0, 0.0, 0.0])

    expected_distance = 1

    calculated_distance = molecool.calculate_distance(r1, r2)

    assert calculated_distance == expected_distance


def test_calculate_distance_type_error():
    """Test that calculate_distance function calculates what we expect"""

    r1 = [1.0, 0.0, 0.0]
    r2 = np.array([0.0, 0.0, 0.0])

    with pytest.raises(TypeError):
        calculated_distance = molecool.calculate_distance(r1, r2)




def test_calculate_angle_1():
    """Test that calculate_angle function calculates what we expect"""

    r1 = np.array([0.0, 1.0, 0.0])
    r2 = np.array([0.0, 0.0, 0.0])
    r3 = np.array([1.0, 0.0, 0.0])

    expected_angle = 90

    calculated_angle = molecool.calculate_angle(r1, r2, r3, True)

    assert calculated_angle == expected_angle


def test_calculate_angle_2():
    """Test that calculate_angle function calculates what we expect"""

    r1 = np.array([0.0, 1.0, 0.0])
    r2 = np.array([0.0, 0.0, 0.0])
    r3 = np.array([1.0, 0.0, 0.0])

    expected_angle = 0.5 * np.pi

    calculated_angle = molecool.calculate_angle(r1, r2, r3, False)

    assert calculated_angle == expected_angle


def test_calculate_angle_3():
    """Test that calculate_angle function calculates what we expect"""

    r1 = np.array([0.0, 1.0, 0.0])
    r2 = np.array([0.0, 0.0, 0.0])
    r3 = np.array([1.0, 0.0, 0.0])

    expected_angle = 0.5 * np.pi

    calculated_angle = molecool.calculate_angle(r1, r2, r3)

    assert calculated_angle == expected_angle



"""
Syntax:

@pytest.mark.parametrize("variable_name1, variable_name2, variable_name3, ..., variable_nameN, expected_answer",
  [ (variable_name1, variable_name2, variable_name3, ..., variable_nameN, expected_answer),
    (variable_name1, variable_name2, variable_name3, ..., variable_nameN, expected_answer)
  ] )
def test_calculate_angle_many(variable_name1, variable_name2, variable_name3, ..., variable_nameN, expected_answer)

"""

@pytest.mark.parametrize("p1, p2, p3, expected_angle", [
   ( np.array([ np.sqrt(2.0)/2.0, np.sqrt(2.0)/2.0, 0.0 ]),  np.array([ 0.0, 0.0, 0.0]), np.array([1.0, 0.0, 0.0]),  45.0 ),
   ( np.array([ 0, 0, -1 ]),  np.array([ 0.0, 1.0, 0.0]), np.array([1.0, 0.0, 0.0]),  60.0 )
   ] )
def test_calculate_angle_many(p1, p2, p3, expected_angle):
    """Test that calculate_angle function calculates what we expect"""

    calculated_angle = molecool.calculate_angle(p1, p2, p3, True)

    assert expected_angle == pytest.approx(calculated_angle)


