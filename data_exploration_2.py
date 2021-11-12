"""
This is to explore trees distributions and other useful information
after cleaning the data
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
if __name__ == '__main__':
      """quantity distribution of each tree species"""
      df_21 = pd.read_csv(r'prepared_data/df_21.csv')
      print(df_21.head(5))
      df_tree = pd.DataFrame({"tree_name": df_21["tree_name"]})
      df_tree['count'] = 1
      df_tree_q = df_tree.groupby("tree_name").sum()
      # dataframe of tree species and quantity: df_tree_q
      df_tree_q = df_tree_q.reset_index()
      df_tree_q = df_tree_q.sort_values(by="count", ascending=False)
      # print out the top 5 most common trees
      # notice that the 'not recorded' indicates unknown species
      # drop the row of unknown species
      df_tree_q = df_tree_q[df_tree_q["tree_name"] != "not recorded"]
      print("The top 5 most common trees in Great London are\n%s",
            df_tree_q.head(5))

      """comparison of quantity of planted trees in different
      boroughs between 2018 and 2021"""

      # data in 2018for bar chart plotting
      df_18 = pd.read_csv(r'prepared_data/df_18.csv')
      df_b_18 = pd.DataFrame({"borough_18": df_18["borough"]})
      df_b_18['count'] = 1
      df_b_18 = df_b_18.groupby("borough_18").sum()
      df_b_18 = df_b_18.reset_index()

      # data in 2021 for bar chart plotting
      df_b_21 = pd.DataFrame({"borough_21": df_21["borough"]})
      df_b_21['count'] = 1
      df_b_21 = df_b_21.groupby("borough_21").sum()
      df_b_21 = df_b_21.reset_index()

      df_plot=df_b_18.merge(df_b_21, left_on="borough_18", right_on="borough_21")
      print(df_plot)

      X = df_plot["borough_18"]
      Y_18 = df_plot["count_x"]
      Z_21 = df_plot["count_y"]

      X_axis =np.arange(len(X))

      plt.bar(X_axis - 0.2, Y_18, 0.4, label='2018')
      plt.bar(X_axis + 0.2, Z_21, 0.4, label='2021')

      plt.xticks(X_axis, X, rotation=90)
      plt.xlabel("Great London Boroughs")
      plt.ylabel("Quantity of trees")
      plt.legend()
      plt.tight_layout()
      plt.show()
