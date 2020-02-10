#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - Infinite loop
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}


/**
 * create_new_zombie - func to create new zombie process
 * @pid: get the pid
 */
void create_new_zombie(pid_t pid)
{
	pid = fork();
	if (pid == 0)
	{
		printf("Zombie process created, PID: %d\n", getpid());
		exit(0);
	}
}

/**
 * main - Creates 5 zombie processes
 * Return: 0
 */
int main(void)
{
	pid_t pid = 0;
	/* Create new Zombie with new func */
	create_new_zombie(pid);
	create_new_zombie(pid);
	create_new_zombie(pid);
	create_new_zombie(pid);
	create_new_zombie(pid);
	/* Call the infinite while function */
	infinite_while();
	return (0);
}
