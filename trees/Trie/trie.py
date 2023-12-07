class TrieNode:
  def __init__(self) -> None:
    self.children = {} # initializing the dictionary
    self.endOfString = False

class Trie:
  def __init__(self) -> None:
    self.root = TrieNode()

  def insertString(self,word): # ----> O(m) where m is the length of the string
    current = self.root # sets the current node to the root
    for i in word:
      ch = i # gets the character
      node = current.children.get(ch) # gets the child node
      if node == None: # checks if there is a corresponding child node in the current node's children
        node = TrieNode()
        current.children.update({ch:node}) # updates the dictionary with the new child node
      current = node # updates the current node
    current.endOfString = True # sets the endOfString attribute to True, like a full stop
    print("Successfully inserted")

  #  must contain end of string at the end ! 
  def searchString(self,word): # ----> O(m) where m is the length of the string
    currentNode = self.root
    for i in word: #looping through each character in the word
      node = currentNode.children.get(i) # gets the child node
      if node == None: # empty node / thing doesn't exist
        return False
      currentNode = node
    
    if currentNode.endOfString == True:
      return True # string has been found
    else:
      return False
    

def deleteString(root, word, index):

  ch = word[index] #Get the current character from the word.
  currentNode = root.children.get(ch) #Get the child node corresponding to the current character.

  canThisNodeBeDeleted = False #Flag to indicate whether the current node can be deleted.


  if len(currentNode.children) > 1:
    """
  If the current node has more than one child,
  meaning other words use it besides the one we're deleting,
  then recursively call the function for the remaining characters
  of the word on the current node's children.
  """
    deleteString(currentNode, word, index+1)
    return False

  if index == len(word) - 1: # If we reached the end of the word and the current node is the last character

    if len(currentNode.children) >= 1: # If the current node has other children (used by other words)
      currentNode.endOfString = False # indicating the specific string is no longer complete here, but keep the node for other words. Node is still needed
      return False
    
    else: # If the current node has no other children (not used by other words)
      root.children.pop(ch) # Remove the current node from the trie
      return True # the entire word and its associated node are deleted

  if currentNode.endOfString == True:
    """
  If the current node marks the end of a word (not necessarily the one being deleted):
    - Recursively call the function for the remaining characters of the word on the current node's children.
    - This ensures any sub-strings of the word being deleted are also removed.
    - Return False as the current node might still be needed for other words.
  """
    deleteString(currentNode, word, index+1)
    return False

  canThisNodeBeDeleted = deleteString(currentNode, word, index+1)
  """
  Recursively call the function for the remaining characters of the word on the current node's children.
  This checks if any sub-strings of the word being deleted are also removed and updates the 'canThisNodeBeDeleted' flag accordingly.
  """

  if canThisNodeBeDeleted == True:
    """
  If the recursive call confirms the current node can be deleted (no other words use it):
    - Remove the current node from the trie using dictionary pop.
    - Return True as the entire word and its associated nodes are deleted.
  """
    root.children.pop(ch)
    return True
  else:
    """
  If other words still use the current node, it cannot be deleted.
  Return False as the deletion is incomplete and the node should remain.
  """
    return False


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("App1")
newTrie.insertString("App2")
newTrie.insertString("Appt")
newTrie.insertString("App3")
deleteString(newTrie.root,"Appt",0)
print(newTrie.searchString("Appt"))