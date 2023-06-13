from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    priority_queue.enqueue({"qtd_linhas": 5, "nome": "file1"})
    priority_queue.enqueue({"qtd_linhas": 1, "nome": "file2"})
    priority_queue.enqueue({"qtd_linhas": 8, "nome": "file3"})
    priority_queue.enqueue({"qtd_linhas": 10, "nome": "file4"})
    priority_queue.enqueue({"qtd_linhas": 2, "nome": "file5"})

    assert len(priority_queue) == 5
    ##

    assert priority_queue.dequeue() == {"qtd_linhas": 1, "nome": "file2"}
    assert priority_queue.dequeue() == {"qtd_linhas": 2, "nome": "file5"}
    assert priority_queue.dequeue() == {"qtd_linhas": 5, "nome": "file1"}
    assert priority_queue.dequeue() == {"qtd_linhas": 8, "nome": "file3"}
    assert priority_queue.dequeue() == {"qtd_linhas": 10, "nome": "file4"}

    assert len(priority_queue) == 0
    ##

    priority_queue.enqueue({"qtd_linhas": 5, "nome": "file6"})
    priority_queue.enqueue({"qtd_linhas": 8, "nome": "file7"})

    assert len(priority_queue) == 2
    ##

    assert priority_queue.dequeue() == {"qtd_linhas": 5, "nome": "file6"}
    assert priority_queue.dequeue() == {"qtd_linhas": 8, "nome": "file7"}

    assert len(priority_queue) == 0
    ##

    priority_queue.enqueue({"qtd_linhas": 5, "nome": "file1"})
    priority_queue.enqueue({"qtd_linhas": 3, "nome": "file2"})
    priority_queue.enqueue({"qtd_linhas": 2, "nome": "file3"})

    assert len(priority_queue) == 3
    ##

    assert priority_queue.dequeue() == {"qtd_linhas": 2, "nome": "file3"}
    assert priority_queue.dequeue() == {"qtd_linhas": 3, "nome": "file2"}
    assert priority_queue.dequeue() == {"qtd_linhas": 5, "nome": "file1"}

    assert len(priority_queue) == 0
    ##

    priority_queue.enqueue({"qtd_linhas": 5, "nome": "file1"})
    priority_queue.enqueue({"qtd_linhas": 4, "nome": "file2"})
    priority_queue.enqueue({"qtd_linhas": 2, "nome": "file3"})

    assert len(priority_queue) == 3
    ##
    assert priority_queue.dequeue() == {"qtd_linhas": 5, "nome": "file1"}
    assert priority_queue.dequeue() == {"qtd_linhas": 4, "nome": "file2"}
    assert priority_queue.dequeue() == {"qtd_linhas": 2, "nome": "file3"}
