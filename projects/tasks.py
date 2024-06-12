"Task classes for MCS 275 Spring 2021 Project 1"
# There is also a document containing discussion of
# this solution.  Please read that for more info.
# Emily Dumas


class Task:
    "Base class for all task types"
    def __init__(self, description):
        "Initialize new Task"
        self.description = description
        self.active = False

    def next_time(self):
        "Return next time task must run (not supported in this base class)"
        raise NotImplementedError(
            "Task not intended to be instantiated directly"
        )

    def run(self):
        "Run the task"
        raise NotImplementedError(
            "Task not intended to be instantiated directly"
        )

    def retire(self, t):
        "Retire task instances up to time t"
        raise NotImplementedError(
            "Task not intended to be instantiated directly"
        )


class OneTimeTask(Task):
    "Task that runs once at a designated time"
    def __init__(self, description, t):
        """Initialize a new OneTimeTask with description `description`
        and run time `t`"""
        super().__init__(description)
        self.active = True
        self.t = t

    def next_time(self):
        "Return next time task must run"
        if not self.active:
            raise Exception("Task is not active")
        return self.t

    def run(self):
        "Run the task"
        print("run: class={} description=\"{}\" time={}".format(
            self.__class__.__name__,
            self.description,
            self.t
        ))

    def retire(self, t):
        "Retire task if its running time is less than or equal to `t`"
        if t >= self.t:
            self.active = False


class RecurringTask(Task):
    "Base class for tasks that run more than once"
    def num_until(self, end):
        "How many times will the task run before time `end`?"
        raise NotImplementedError(
            "RecurringTask not intended to be instantiated directly"
        )


class BoundedRecurringTask(RecurringTask):
    "Task that runs at times in a finite arithmetic progression"
    def __init__(self, description, start, gap, n):
        """Initialize a recurring task that runs first at time `start`, again at `start`+`gap`, 
        and so on, until it has run `n` times"""
        super().__init__(description)
        self.t_next = start
        self.gap = gap
        self.times_left = n
        self.active = self.times_left > 0

    def run(self):
        "Run the task"
        if not self.active:
            raise Exception("task is not active")
        print("run: class={} description=\"{}\" time={}".format(
            self.__class__.__name__,
            self.description,
            self.t_next
        ))

    def next_time(self):
        "Return next time task must run"
        if self.active:
            return self.t_next
        else:
            raise Exception("task is not active")

    def num_until(self, end):
        "How many times will the task run before time `end`?"
        if end < self.t_next:
            # The next instance is after `end`, so the answer is zero
            return 0
        # How many instances if the task ran forever
        n = 1 + ((end-self.t_next) // self.gap)
        # Actual number is clipped by self.times_left
        return min(n,self.times_left)

    def num_total(self):
        "How many times will the task run (excluding retired instances)?"
        return self.times_left

    def retire(self, t):
        "Retire instances of the task up to and including time `end`"
        k = self.num_until(t)
        self.t_next += k*self.gap
        self.times_left -= k
        self.active = self.times_left > 0


class UnboundedRecurringTask(RecurringTask):
    "Task that runs at times in an infinite arithmetic progression"
    def __init__(self, description, start, gap):
        """Initialize a recurring task that runs first at time `start`, again at `start+gap`, 
        `start+2*gap`, and so on, forever."""
        super().__init__(description)
        self.t_next = start
        self.gap = gap
        self.active = True

    def run(self):
        "Run the task"
        print("run: class={} description=\"{}\" time={}".format(
            self.__class__.__name__,
            self.description,
            self.t_next
        ))

    def next_time(self):
        "Return next time task must run"
        return self.t_next

    def num_until(self, end):
        "How many times will the task run before time `end`?"
        if end < self.t_next:
            # The next instance is after `end`, so the answer is zero
            return 0
        return 1 + ((end-self.t_next) // self.gap)

    def retire(self, t):
        "Retire instances of the task up to and including time `t`"
        k = self.num_until(t)
        self.t_next += k*self.gap
