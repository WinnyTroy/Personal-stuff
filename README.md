# Personal-stuff

  
troy is the basic setup of a blogging site. It has been structured using HTML/CSS.  It also uses Bootsrap for front-end styling.
![data_flow](https://user-images.githubusercontent.com/11174326/49939360-b3ad8d80-feed-11e8-9eba-99b1d44e7a4b.png)


|**Variable** | **Aggregations**         |
| ------------- | ----------- |
| Enumerated Structures             | The number of structures as they are in the spray area shape file.|
| Not sprayable structures          | The number of structures in the field that were found not to be sprayable.     |
| Duplicate sprayed structures      | When a structure has been reported more than one time with the spray status sprayed (if                                      IDXYZ appears twice as sprayed, the count of duplicates will be 1, if it appears 3 times                                      the count will be 2, ... etc.)     |
| Structures on the ground     | Enumerated structures subtract number of not sprayable structures + number of new                                               structureres + number of duplicate structures that have been sprayed     |
| Found     | Number of all unique records that are sprayable add Number of structures that were sprayed                                     that are not part of the unique record set (i.e the number of duplicates)     |
| Visited Sprayed     | Number of all unique records that have the spray status "sprayed"     |
| Spray Effectiveness     | Percentage of  Visited Sprayed / Structures on the ground     |
| Found Coverage     | Percentage of Found / Structures on the ground     |
| Close     | Percentage of Visited Sprayed / Found     |
