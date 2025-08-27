# Report

Please answer the questions below. Make sure to ask questions if you have them. 


For all these questions, it is recommended you use the python interpreter and try out the code.  You can also use the python visualizer to help you visualize the code.  You can find the visualizer here: [http://www.pythontutor.com/visualize.html#mode=edit](http://www.pythontutor.com/visualize.html#mode=edit)


1. Correct the following loop.
   ```python
   value = None
   while value == "quit":
       value = input("Enter a value or quit: ")
       print(value)
   ```
    ```python
    ## put your corrected code below this line

    ```

2. The above code uses a None value to initialize the input variable. This works because python can let a variable be multiple types, but in some languages, you would have to match the type. Assuming you had to match the type (str), what would be a good default input value, that could never cause the loop to not run at least once? Provide reasoning for your logic as there are multiple correct answers. With that said, there is one that is more 'standard' than the rest, so feel free to openly discuss options that come to mind (you do not have to come up with the standard answer, but try to!). 
   

3. Write a small loop that will keep repeating until someone 
   enters a number greater than 0, and less than 5. It has to be
   whole numbers (hint: look up .isnumeric() from the team activity).

   ```python
   ## put your code here
   ```

4. Draw a flow diagram for your solution to #3

5. Looking back at homework #2, we actually had a type of 'loop' in the provided code (look near the main function). First copy the bit of code that causes the loop.
    ```python
    # code here
    ```
    Now: what would be some of the pros and cons of looping in such a way (think about 'frames' you see in the python visualizer)?

6. Thinking about edge cases, it is very common to get an off-by-one (OB1) error with loops. 
   Create two test cases (just as examples/inputs) for the following code. They 
   should both be 'correct' cases, but one of them should uncover the error in the code.

   ```python
    def count_backwards(value: int) -> None:
        """ Counts from value to 0, printing even values until 10 (including 10), and 
        then odd values."""
       counter = value
       while counter >= 0:
          if counter > 10:
            if counter % 2 == 0:
                print(counter)
          else:
            if counter % 2 == 1:
                print(counter)
          counter -= 1
   ```
   * Example test one:
   * Example test two:

 7. When thinking of these edge cases and OB1 errors, it is common to say one should test
    every condition plus-minus 1. In your opinion, is this beneficial? Why or why not?


## Application Runs
The following questions will require you run the Accessibility Analyzer to generate results. 

> Do display colors in the markdown, you will have to switch to standard html and built in styles. For example, the code below, will generate a 'teal' block with black text. Feel free to copy and past the block, only modifying the color values as you need.   
> ![#4ECDC4](https://placehold.co/15x15/4ECDC4/4ECDC4.png) `#4ECDC4`

1. Check WCAG contrast compliance - pick two colors to run with the WCAG option (1) in the color app.
   
   1.1  What two colors did you pick (use the color block but update values)
      * ![#CCCCCC](https://placehold.co/15x15/CCCCCC/CCCCCC.png) `#CCCCCCC`
      * ![#CCCCCC](https://placehold.co/15x15/CCCCCC/CCCCCC.png) `#CCCCCCC`


   1.2  What was the result, use the block below to copy and paste the result of the test
   ```
   copy and paste here
   ```

   1.3 Did the results show what you though?  

   1.4 Explore colors until you can find two that pass all the WCAG compliance categories.  What two did you find?
       
      * ![#CCCCCC](https://placehold.co/15x15/CCCCCC/CCCCCC.png) `#CCCCCCC`
      * ![#CCCCCC](https://placehold.co/15x15/CCCCCC/CCCCCC.png) `#CCCCCCC`
  
2.  Analyze color properties - pick a color to run with this option

    2.1 What color did you pick?
    
       * ![#CCCCCC](https://placehold.co/15x15/CCCCCC/CCCCCC.png) `#CCCCCCC`
    
    2.2 What are the results, copy and paste them below.
     ```
     copy and paste here
     ```

3. Test colorblind accessibility - pick two colors to analyze. You need to find two that would end up being the same color (or close to the same color) depending on the type of color blindness. 

    3.1 What colors did you pick?

     * ![#CCCCCC](https://placehold.co/15x15/CCCCCC/CCCCCC.png) `#CCCCCCC`
     * ![#CCCCCC](https://placehold.co/15x15/CCCCCC/CCCCCC.png) `#CCCCCCC`

    3.2 What were the results for each of them - copy and paste below in each block
    ```
     color 1: copy and paste here
    ```
    ```
     color 2: copy and paste here
    ```

    3.3 Now run modified (by the colorblindness type) colors through the Check WCAG contrast compliance option. Spoiler, at least one should fail, but there may be rare cases it passes. You should also run the original colors through the Check WCAG.
 
     * ![#CCCCCC](https://placehold.co/15x15/CCCCCC/CCCCCC.png) `#CCCCCCC`
     * ![#CCCCCC](https://placehold.co/15x15/CCCCCC/CCCCCC.png) `#CCCCCCC`

    3.4 What were the results for that test
    ```
      copy and paste here
    ```

    3.5 Did your your original colors pass better than the modified color blindness ones?


4. Did running this application help you learn anything new about html / web colors? If so, what?


> Make sure to look at your rendered document in github!  
> Before you turn it in for grading.


## Deeper Thinking

Human Computer Interaction (HCI) is a field within computer science that focuses on how people interact with technology systems. It involves designing interfaces and experiences by continuously communicating with stakeholders, conducting research into effective design patterns, and questioning assumptions about user behavior and needs. 

HCI emphasizes inclusive design - creating systems that work for people across different abilities, backgrounds, and contexts. This approach extends beyond basic accessibility compliance to consider the full spectrum of human diversity. Whether designing web applications, operating systems, VR/AR experiences, or video games, HCI practitioners integrate user research and inclusive principles throughout the development process.

HCI intersects with virtually all domains of computer science and relies heavily on collaboration between designers, developers, researchers, and clients to build systems that better serve diverse communities.

**Assignment:**

Research HCI and UX design to understand the field better. Find at least three credible sources (academic articles, professional publications, or reputable industry resources) and provide links to them. 

After reviewing your sources, write a reflection addressing these questions:

1. Based on your research, how would you define HCI and its core principles?

2. Why is inclusive design particularly important in computer science and HCI? Consider both ethical and practical implications.

3. How might the accessibility concepts you learned in this assignment (color contrast, colorblindness considerations) connect to broader HCI principles?

Your reflection should demonstrate understanding of the field while incorporating insights from your research sources. Write in paragraph form rather than bullet points, and aim for thoughtful analysis rather than simple summaries.
