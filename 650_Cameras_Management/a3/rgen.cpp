#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <cmath>
#include <stdio.h>
#include <fstream>
#include <vector>
#include <fcntl.h>

using namespace std;

// declaration
class Point;
class Line;
class Street;
class Map;
Map* randomGenerator();	
int sRandGen();
int lRandGen();
Map* nRandGen(int, Map*);
Point* cRandGen(Point*);
int isLineValid(Line* l1, Line* l2);
bool parallel(Line*, Line*);
bool oneStreetCheck(Street* street, Line* line);
bool twoStreetsCheck(Map* map, Line* line);
void attemptsOver25(int);
void rmStreets(Map*);
string randomName(int);
string printPoints(vector<Point*>);


// variables
int count = 0;	// counting time

int ks = 10, kn = 5, kl = 5, kc = 20;	// default of -s, -n. -l. -c
int sRand, nRand, lRand, cRand1, cRand2;	// store the random number from -s, -n and -l


class Point{
private:
	double x;
	double y;
public:
	Point(double x, double y){	//constructor
		this->x = x;
		this->y = y;
	}
	double getX(){
		return this->x;
	}
	void setX(double x){
		this->x = x;
	}
	double getY(){
		return this->y;
	}
	void setY(double y){
		this->y = y;
	}
	bool isEqual(Point *pt){
		return pt->getX() == this->x and pt->getY() == this->y;
	}
        
    bool isInList(vector<Point*> pt_list){
		if (pt_list.empty()){
			return false;
		}
        for (Point* pt : pt_list){
			if (this->isEqual(pt)){
				return true;
			}
		}
        return false;
	}

	double distance(Point *pt){
		return sqrt(pow(this->getY() - pt->getY(),2) + pow(this->getX() - pt->getX(), 2));
	}

	string printPoint(){	// we need integer number for python input
		string str = "(" + to_string(int(this->getX())) + "," + to_string(int(this->getY())) + ")"; 
		return str;
	}
};

class Line{
private:
	Point* src;
	Point* dst;
public:
	Line(Point* src, Point* dst){
		this->src = src;
		this->dst = dst;
	}
	Point* getSrc(){
		return this->src;
	}
	Point* getDst(){
		return this->dst;
	}
	void setSrc(Point* src){
		this->src = src;
	}
	void setDst(Point* dst){
		this->dst = dst;
	}
	bool isEqual(Line* line){
		if ((line->src->isEqual(this->src) and line->dst->isEqual(this->dst))||(line->src->isEqual(this->dst) and line->dst->isEqual(this->src))){
			return true;
		} else {
			return false;
		}
	}

    bool isInList(vector<Line> line_list){
		if (line_list.empty()){
			return false;
		}
		for (int i = 0; i < line_list.size(); i++){
			if (this->isEqual(&line_list[i])){
				return true;
			}
		}
		return false;
	}

	double is_vertical(){
		if (this->getSrc()->getX() == this->getDst()->getX()){
			return true;
		}
        return false;
	}
        
	double gradient(){
		// if (!this->is_vertical()){
		double slope = (this->getDst()->getY() - this->getSrc()->getY()) / (this->getDst()->getX() - this->getSrc()->getX());
		return slope;
		// }
	}

	string printLine(){
		string str = "(" + this->getSrc()->printPoint() + "," + this->getDst()->printPoint() + ")";
		return str;
	}

	double distance(){
		return sqrt((pow(this->getSrc()->getY() - this->getDst()->getY(),2)) + (pow(this->getSrc()->getX() - this->getDst()->getX(),2))); 
	}
};

Point* intersect(Line* line1, Line* line2){
    double x1 = line1->getSrc()->getX();
	double y1 = line1->getSrc()->getY();
	double x2 = line1->getDst()->getX();
	double y2 = line1->getDst()->getY();

    double x3 = line2->getSrc()->getX();
	double y3 = line2->getSrc()->getY();    
	double x4 = line2->getDst()->getX();
	double y4 = line2->getDst()->getY();

    if (x1 == x3 && y1 == y3){
		return new Point(x1, y1);
	}
        
    if (x1 == x4 && y1 == y4){
		return new Point(x1, y1);
	}
        
    if (x2 == x3 && y2 == y3){
		return new Point(x2, y2);
	}
        
    if (x2 == x4 && y2 == y4){
		return new Point(x2, y2);
	}
        
    if (!parallel(line1, line2)){
		double area1 = (x3 - x1) * (y2 - y1) - (x2 - x1) * (y3 - y1);
        double area2 = (x4 - x1) * (y2 - y1) - (x2 - x1) * (y4 - y1);

        if (area1 * area2 > 0){
            return NULL;
		}

        double area3 = (x2 - x3) * (y4 - y3) - (x4 - x3) * (y2 - y3);
        double area4 = (x1 - x3) * (y4 - y3) - (x4 - x3) * (y1 - y3);

        if (area3 * area4 > 0){
            return NULL;
		}

        double xnum = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4));
        double xden = ((x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4));
        double xcoor = xnum / xden;

        double ynum = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4);
        double yden = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);
        double ycoor = ynum / yden;

        return new Point(xcoor, ycoor);
	}else{
		return NULL;
	}
}

class Street{	
private:
	string name;
	vector<Line*> streetLines;
public:
	Street(string name){
		this->name = name;
	}
	string getName(){
		return this->name;
	}
	vector<Line*> getStreetLines(){
		return this->streetLines;
	}
	void addEdges(Line* edge){
		this->streetLines.push_back(edge);
	}

	string printStreet(){
		string str = "";
		for (int i=0; i < this->streetLines.size(); i++){
			if (i != this->streetLines.size()){
				str = str + this->streetLines[i]->printLine() + " ";
			}
			else{
				str = str + this->streetLines[i]->printLine() + "\n";
			}
		}
		return str;
	}
};

class Map{	// containing/storing all streets
private:
	vector<Street*> streets;
public:
	vector<Street*> getStreets(){
		return this->streets;
	}
	void addStreets(Street* street){
		this->streets.push_back(street);
	}
	void reset(){
		this->streets.clear();
	}
};

Map* map1 = new Map();

int main(int argc, char** argv) {
	opterr = 0; 	// Looks important!
	int opt = 0;

	while((opt = getopt(argc, argv, "s:n:l:c:")) != -1){
		switch(opt){
			case 's':
				if (atoi(optarg) >= 2){
					ks = atoi(optarg);
				} else{
					cerr << "Error: The number of streets cannot be less than 2." << endl;
					exit(0);
				}
				break;
			case 'n':
				if (atoi(optarg) >= 1){
					kn = atoi(optarg);
				} else{
					cerr << "Error: The number of line segments in a street cannot be less than 1." << endl;
					exit(0);
				}
				break;
			case 'l':
				if (atoi(optarg) >= 5){
					kl = atoi(optarg);
				} else{
					cerr << "Error: The number of waiting seconds cannot be less than 5 seconds." << endl;
					exit(0);
				}
				break;
			case 'c':
				if (atoi(optarg) >= 1){
					kc = atoi(optarg);
				} else{
					cerr << "Error: Value K cannot be less than 1." << endl;
					exit(0);
				}
				break;
			case '?':
				if (optopt == 's' || optopt == 'n' || optopt == 'l' || optopt =='c'){
					cerr << "Error: Arguments are missing." << endl;
					return 1;
				} else{
					cerr << "Error: The option is not allowed." << endl;
					return 1;
				}
			default:
				return 0;
		}
	}
	
	while(true){
		Map* wholeMap = randomGenerator();
		sleep(lRand);
		// sleep(1);
		rmStreets(wholeMap);
		wholeMap->reset();
	}	
}

bool parallel(Line* line1, Line* line2){
	if (line1->is_vertical()){
		if (line2->is_vertical()){
			return true;
		} else{
			return false;
		}
	}
	else if (line2->is_vertical()){
		return false;
	}
	if (line1->gradient() != line2->gradient()){
		return false;
	}
	return true;
}

int isLineValid(Line* l1, Line* l2){	// return 0 if overlap (not allowed), 
										// return 1 if intersect(used for checking self-intersect - sometimes allowed), 
										// return 2 if parallel or no intersect(allowed)
	if (l1->isEqual(l2)){
		return 0;
	}
	if (!parallel(l1, l2)){
		Point* intersect_pt = intersect(l1, l2);
		if (intersect_pt == NULL){
			return 2;
		}
		return 1;
	}
	else{	// parallel or overlap
		Point* l1_src = l1->getSrc();
		Point* l1_dst = l1->getDst();
		Point* l2_src = l2->getSrc();
		Point* l2_dst = l2->getDst();

		double distance_l1 = l1->distance();
		double distance_l2 = l2->distance();
		if (abs(distance_l1 - (l1_src->distance(l2_src) + l1_dst->distance(l2_src))) < 0.001) {
			if (l1_src->isEqual(l2_src) || l1_dst->isEqual(l2_src)){
				if (abs(distance_l1 - (l1_src->distance(l2_dst) + l1_dst->distance(l2_dst))) < 0.001) {
					return 0;
				} else{
					return 1;
				}
			} 
			return 0;
		}
		if (abs(distance_l1 - (l1_src->distance(l2_dst) + l1_dst->distance(l2_dst))) < 0.001) {
			if (l1_src->isEqual(l2_dst) || l1_dst->isEqual(l2_dst)){
				if (abs(distance_l1 - (l1_src->distance(l2_src) + l1_dst->distance(l2_src))) < 0.001) {
					return 0;
				} else{
					return 1;
				}
			} 
			return 0;	
		}
		if (abs(distance_l2 - (l2_src->distance(l1_dst) + l2_dst->distance(l1_dst))) < 0.001) {
			if (l2_src->isEqual(l1_dst) || l2_dst->isEqual(l1_dst)){
				if (abs(distance_l2 - (l2_src->distance(l1_src) + l1_dst->distance(l1_src))) < 0.001) {
					return 0;
				} else{
					return 1;
				}
			} 
			return 0;	
		}
		if (abs(distance_l2 - (l2_src->distance(l1_src) + l2_dst->distance(l1_src))) < 0.001) {
			if (l2_src->isEqual(l1_src) || l2_dst->isEqual(l1_src)){
				if (abs(distance_l2 - (l2_src->distance(l1_src) + l1_dst->distance(l1_src))) < 0.001) {
					return 0;
				} else{
					return 1;
				}
			} 
			return 0;	
		}
		return 2;
	}
}

bool oneStreetCheck(Street* street, Line* line){	// Check whether the line is valid in its street (check self-intersect and overlap)
	int typeOfLines = 0;
	if(street->getStreetLines().size() == 0){
		return true;
	}
	for (Line* l : street->getStreetLines()){
		
		typeOfLines = isLineValid(l, line);
		// cout << "type:" << typeOfLines << endl;
		if (typeOfLines == 0){
			return false;
		}
		if (typeOfLines == 1){
			if (l == street->getStreetLines().back()){
				continue;
			}
			else{
				return false;	// cannot self-intersect
			}
		}
		if (typeOfLines == 2){
			if (l == street->getStreetLines().back()){
				cerr << "Error: Something wrong "<< endl;
				exit(1);
				return false;
			}
			continue;
		}
		else{
			cerr << "Error: Something wrong!" << endl;
			exit(1);
			return false;
		}
	}
	return true;
}

bool twoStreetsCheck(Map* map, Line* line){	//check overlaps
	int typeOfLines = 0;
	if (map->getStreets().size() == 0){
		return true;
	}
	for (Street* st : map->getStreets()){
		for (Line* l: st->getStreetLines()){
			typeOfLines = isLineValid(l, line);
			if (typeOfLines == 0){
				return false;
			}
			if (typeOfLines == 1){
				continue;
			}
			if (typeOfLines == 2){
				continue;
			}
			else{
				cerr << "Error: Something wrong!" << endl;
				exit(1);
				return false;
			}
		}
	}
	return true;
}

string randomName(int n=6){
	// Credit from: https://www.geeksforgeeks.org/program-generate-random-alphabets/
	int MAX = 26;
	char alphabet[MAX] = { 'a', 'b', 'c', 'd', 'e', 'f', 'g',
						'h', 'i', 'j', 'k', 'l', 'm', 'n',
						'o', 'p', 'q', 'r', 's', 't', 'u',
						'v', 'w', 'x', 'y', 'z' };
 
    string name = "";
	unsigned int random_value = 0;
	size_t size = sizeof(random_value);

	// I don't know why ifstream to use urandom cannot be used in loop, so I changed another way to generate random numbers.
	// Credit from https://security.stackexchange.com/questions/184210/how-to-correctly-use-dev-urandom-for-random-generation/184211
	int times = 0;
	int fd = open("/dev/urandom", O_RDONLY);
	while (times < n){
		
		if(fd == -1){
			cerr << "Error: Failed to read from /dev/urandom." << endl;
			return "";
		} 
		read(fd, (char *)&random_value, size);
		name += alphabet[random_value % MAX]; 
		times++;
	}
	close(fd);
	return name;
}

Map* randomGenerator(){
	sRand = sRandGen();
	lRand = lRandGen();
	Map* wholeMap = nRandGen(sRand, map1);
	return wholeMap;
}

void rmStreets(Map* m){
	vector<Street*> streets = m->getStreets();
	for (Street* st:streets){
		vector<Line*> lines = st->getStreetLines();
		string st_name = st->getName();
		cout << "rm \"" << st_name << "\"" << endl;
	}

}

Map* nRandGen(int streets_nums, Map* map1){
	unsigned int random_value = 0;
	size_t size = sizeof(random_value);
	int streets_no = 0;
	vector<Point*> points;

	
	int fd = open("/dev/urandom", O_RDONLY);
	while (streets_no < streets_nums){	// creating streets in map
		Street* st = new Street(randomName());
		points.clear();
		if(fd == -1){
			cerr << "Error: Failed to read from /dev/urandom." << endl;
			exit(1);
		} 
		read(fd, (char *)&random_value, size);
		nRand = random_value % (kn) + 1; // range in [1, kn]
		Point* pt1 = new Point(0,0);
		pt1 = cRandGen(pt1);

		points.push_back(pt1);

		for (int i = 0; i < nRand; i++){	// creating edges in one street
			Point* pt2 = new Point(0,0);
			pt2 = cRandGen(pt2);
			Line* line = new Line(points.back(), pt2);	
			while(count <= 25 && (pt1->isEqual(pt2) || !oneStreetCheck(st, line) || !twoStreetsCheck(map1, line))){
				count++;
				pt2 = cRandGen(pt2);
				line->setDst(pt2);
			}
			
			attemptsOver25(count);
			points.push_back(pt2);
			st->addEdges(line);
			count = 0; // everytime an edge added is correct, reset the count
		}
		map1->addStreets(st);
		streets_no++;
		cout << "add \"" << st->getName() << "\" " << printPoints(points);
	}
	close(fd);
	points.clear();
	cout << "gg" << endl;
	return map1;
}

string printPoints(vector<Point*> points_list){
	string str = "";
	for (int i = 0; i < points_list.size(); i++){
		if (points_list.size()-1 == i){
			str = str + points_list[i]->printPoint() + "\n";
		}
		else{
			str = str + points_list[i]->printPoint() + " ";
		}
	}
	return str;
}

Point* cRandGen(Point* pt){
	unsigned int random_value = 0;
	size_t size = sizeof(random_value);
	int streets_no = 0;
	int fd = open("/dev/urandom", O_RDONLY);

	if(fd == -1){
		cerr << "Error: Failed to read from /dev/urandom." << endl;
		exit(1);
	} 
	read(fd, (char *)&random_value, size);
	cRand1 = random_value % (2*kc + 1) - kc; // range in [-kc, kc] <= can be converted from [0. 2kn]

	read(fd, (char *)&random_value, size);
	cRand2 = random_value % (2*kc + 1) - kc; // range in [-kc, kc] <= can be converted from [0. 2kn]

	pt->setX(cRand1);
	pt->setY(cRand2);
	close(fd);
	return pt;
}

int sRandGen(){
		// Credit from: https://stackoverflow.com/questions/35726331/c-extracting-random-numbers-from-dev-urandom
	unsigned int random_value;
	size_t size = sizeof(random_value);
	ifstream urandom("/dev/urandom");	//open stream
	if(urandom){ //check if the stream is open

		// Randomly set up the number of streets
		urandom.read(reinterpret_cast<char*>(&random_value), sizeof(size));	// read from urandom
		if(urandom){	// check if stream is ok, read successed
			sRand = random_value % (ks - 2 + 1) + 2;	// range in [2, ks]
		} else{
			cerr << "Error: Failed to read from /dev/urandom." << endl;
			exit(1);
		}
	} else{	// Open Failed
		cerr << "Error: Failed to open /dev/urandom." << endl;
		exit(1);
	}
	urandom.close();
	return sRand;
}

int lRandGen(){
		// Credit from: https://stackoverflow.com/questions/35726331/c-extracting-random-numbers-from-dev-urandom
	unsigned int random_value;
	size_t size = sizeof(random_value);
	ifstream urandom("/dev/urandom");	//open stream
	if(urandom){ //check if the stream is open
		// Randomly set up the waiting time
		urandom.read(reinterpret_cast<char*>(&random_value), sizeof(size));	// read from urandom
		if(urandom){	// check if stream is ok, read successed
			lRand = random_value % (kl - 5 + 1) + 5;	// range in [5, kl]
		} else{
			cerr << "Error: Failed to read from /dev/urandom." << endl;
			exit(1);
		}
	} else{	// Open Failed
		cerr << "Error: Failed to open /dev/urandom." << endl;
		exit(1);
	}
	urandom.close();
	return lRand;
}

void attemptsOver25(int count){
	if (count > 25){
		cerr << "Error: Attempted over 25 times." << endl;
		exit(1);
	}
}

