import numpy as np
import string

class edit_distance:
  def __init__(self):
    """
      ref = "the dog is under the table"
      pred = "The dog is the fable"
      score = model.fit(pred, ref)
        ----> 0.33
      model.get_detail()
        ----> {'delete': 0, 'insert': 1, 'substitution': 1, 'same words': 4}

    """
    pass


  def get_score(self, pred, ref):
    """
      We used the distance matrix to calculate the number of titles below : 
        1 --- > delete
        2 --- > insert
        3 --- > substitution

        we use backtrcing method and dynamic programming 

    


      Define the numbers used 
        1 -- > same words
        2 ---> insert
        3 ---> delete
        4 ---> substitution
    """

    costs = np.zeros((1 + len(pred), 1 + len(ref)))
    self.backtrace = np.zeros((1 + len(pred), 1 + len(ref)))

    costs[0] = [j for j in range(0, len(ref) + 1)]
    self.backtrace[0][ : ] = 2


    costs[ : , 0] = [j for j in range(0, len(pred) + 1)]
    self.backtrace[ : ][0] = 3

    self.backtrace[0][0] = 10 #None


    for row in range(1 , len(pred) + 1):
      for  col in range(1, len(ref) + 1):
        if pred[row - 1] == ref[col - 1]:
          costs[row][col] = costs[row - 1][col - 1]
          self.backtrace[row][col] = 1
        else:
          substitution = costs[row - 1][col - 1]
          delete = costs[row - 1][col]
          insert = costs[row][col - 1]
          fainal_cost = min(delete, insert, substitution)
          costs[row][col] = fainal_cost + 1

          if fainal_cost == delete:
            self.backtrace[row][col] = 3
          elif fainal_cost == insert:
            self.backtrace[row][col] = 2
          elif fainal_cost == substitution:
            self.backtrace[row][col] = 4

    return (costs[-1][-1]) / len(ref)


  def get_detail(self):


    i, j = len(pred), len(ref)
    self.num_same , self.num_del, self.num_sub, self.num_ins = 0, 0, 0, 0

    while i > 0 or j > 0:
      if self.backtrace[i][j] == 1:
        i -= 1
        j -= 1
        self.num_same += 1

      if self.backtrace[i][j] == 4:
        i -= 1
        j -= 1
        self.num_sub += 1


      if self.backtrace[i][j] == 2:
        j -= 1
        self.num_ins += 1

      if self.backtrace[i][j] == 3:
        i -= 1
        self.num_del += 1

        
    return {
      "delete" : self.num_del,
      "insert" : self.num_ins,
      "substitution" : self.num_sub,
      "same words" : self.num_same
    }


