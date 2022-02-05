// Credit: Sources from https://git.uwaterloo.ca/ece650-f2021/cpp/-/blob/master/using_pipe.cpp
// https://git.uwaterloo.ca/ece650-f2021/cpp/-/blob/master/using_fork.cpp
// https://git.uwaterloo.ca/ece650-f2021/cpp/-/blob/master/using_exec.cpp
#include <iostream>
#include <unistd.h>
#include <istream>
#include <string>
#include <vector>
#include <sys/types.h>
#include <sys/wait.h>

using namespace std;

int main (int argc, char **argv) {
    vector<pid_t> kids;
    pid_t pid;
    int fd1[2]; // pipe1 between rgen and a1
    int fd2[2]; // pipe2 between a1 and a2

	opterr = 0;	// this is very important - without this, it would be like: 
				// ./ece650-a3: option requires an argument -- 's' (this sentense will shown on if not put opterr = 0)
				//  Error: Arguments are missing.
    pipe(fd1);
    pipe(fd2);

    int opt = 0;
	int ks = 10, kn = 5, kl = 5, kc = 20; // default
    while((opt = getopt(argc, argv, "s:n:l:c:")) != -1){
		switch(opt){
			case 's':
				ks = atoi(optarg);
				if (ks < 2){
					cerr << "Error: The number of streets cannot be less than 2." << endl;
					exit(0);
				} 
				break;
			case 'n':
				kn = atoi(optarg);
				if (kn < 1){
					cerr << "Error: The number of line segments in a street cannot be less than 1." << endl;
					exit(0);
				}
				break;
			case 'l':
				ks = atoi(optarg);
				if (ks < 5){
					cerr << "Error: The number of waiting seconds cannot be less than 5 seconds." << endl;
					exit(0);
				}
				break;
			case 'c':
				kc = atoi(optarg);
				if (kc < 1){
					cerr << "Error: Value K cannot be less than 1." << endl;
					exit(0);
				}
				break;
			case '?':
				if (optopt == 's' || optopt == 'n' || optopt == 'l' || optopt =='c'){
					cerr << "Error: Arguments are missing." << endl;
					exit(0);
				} else{
					cerr << "Error: The option is not allowed." << endl;
					exit(0);
				}
		}
    }

    pid = fork();
    // child one - communicate between rgen and a1
    if (pid == 0){
        // redirect 
        close(fd1[0]);
        dup2(fd1[1], 1);  // 1 for WRITE-END, 0 FOR READ-END
        close(fd1[1]);
        
		// pipe fd1:   a1 (read) <======> rgen (write)
        return execv("./rgen", argv);   
    } else if (pid < 0){
        cerr << "Error: Fork did not generate!" << endl;
        exit(0);
    }

    kids.push_back(pid);

    pid = fork();

    // child two - communicate between rgen and a1, && a1 and a2   
    if (pid == 0){
		// pipe fd1:   a1 (read) <======> rgen (write)
		close(fd1[1]);
        dup2(fd1[0], 0);     
        close(fd1[0]);
        
		// pipe fd2:   a2 (read) <======> a1(output) (write)
		close(fd2[0]);
        dup2(fd2[1], 1);    
        close(fd2[1]);

        // now we need to implement python arguments
        char *a1Argv[3];
        a1Argv[0] = (char*) "/usr/bin/python3";
        a1Argv[1] = (char*) "./ece650-a1.py";
        a1Argv[2] = nullptr;
        return execv("/usr/bin/python3", a1Argv);
    }else if (pid < 0){
        cerr << "Error: Fork did not generate!" << endl;
        exit(0);
    }

    kids.push_back(pid);


    // child 3 - communicate between a1 and a2
    pid = fork();
    
    if (pid == 0){
        // pipe fd2:   a2 (read) <======> a1(output) (write)
		close(fd2[1]);
        dup2(fd2[0], 0);    
        close(fd2[0]);

		// implement a2 cpp arguments
		char *a2Argv[2];
		a2Argv[0] = (char*)"./ece650-a2";
		a2Argv[1] = nullptr;

        return execv("./ece650-a2", a2Argv);
    }else if (pid < 0){
        cerr << "Error: Fork did not generate!" << endl;
        exit(0);
    }

    kids.push_back(pid);


    // Parent Process (parent process read a1 output)
	close(fd2[0]);
    dup2(fd2[1],1);
    close(fd2[1]);

	while(true){
		string line;
		getline(cin, line);
		// cout << line << endl;
		if (cin.eof()){
			break;
		}
		if (line.size()>0){
			cout << line << endl;
		}
	}
	close(fd1[1]);
	close(fd2[1]);

    // send kill signals to all children
    for (pid_t k : kids){
		// cout << "waiting for child process to terminate" << endl
        int status;
        kill(k, SIGTERM);
        waitpid(k, &status, 0);
    }

    return 0;
}
