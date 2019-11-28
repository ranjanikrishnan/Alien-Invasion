# Alien Invasion - Python

## Problem statement

- Simulation of a non-existent world 'X' where mad aliens are about to invade the earth.

- Input to the program would be as follows:

	- number of aliens

	- a file which contains the list of city names with one city per line followed by directions (north, south, east or west). Each one represents a road to another city that lies in that direction. For eg:
	   ```
		Foo north=Bar west=Baz south=Qu-ux
		Bar south=Foo west=Bee
	  ```
- The aliens start out in random cities and wander along randomly. In each iteration, they can travel in any of the directions leading out of a city. Whenever two aliens end up in the same city, they fight and destroy the city. When a city is destroyed, it is removed from the map and so are any road that leads in or out of it.

- The simulation ends when all aliens are destroyed or each alien has moved at least 10,000 times.

- A message in print out whenever a city is destroyed. Once the simulation has ended, the final world map is printed out in the same format as the input file.

  

## How to get it running?
- Install the dependent packages from requirements.txt

`pip install -r requirements.txt`

- Use the following command for running options

` python src/alien_invasion.py -h`

- Following is a sample run of the simulation

` python src/alien_invasion.py ./input/input_2.txt 5 `

> Tested on python version 3.6

## Assumptions

- City names will never contain numeric characters.
- In the input file, if there's a city A which has a road to B, assume that there is also a road from city B to A.
- There can be more than 2 aliens in a city which causes them to kill themselves and the city is destroyed.
- When the aliens are unleashed they could end up fighting before their first move.

## Demo

- Sample input:

` python src/alien_invasion.py ./input/input_1.txt 5 `

- Sample output:
  
```
Bar has been destroyed by alien 1, and alien 3.

Foo has been destroyed by alien 2, and alien 4.

All cities destroyed!
```

## Tests

- All the tests are under the test folder.
- Following is a sample run of a test.

`pytest test/test_read_map.py`

