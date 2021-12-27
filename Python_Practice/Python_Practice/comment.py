{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100\n",
      "\n",
      "   This function is to square the number\n",
      "   __doc__ this is an attribute to print the docstring about the function\n",
      "   \n"
     ]
    }
   ],
   "source": [
    "def square(num):\n",
    "\n",
    "   '''\n",
    "   This function is to square the number\n",
    "   __doc__ this is an attribute to print the docstring about the function\n",
    "   '''\n",
    "\n",
    "   return num*num\n",
    "\n",
    "print(square(10))\n",
    "\n",
    "print(square.__doc__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<function __main__.square(num)>"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "square #press shift+tab for description"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
