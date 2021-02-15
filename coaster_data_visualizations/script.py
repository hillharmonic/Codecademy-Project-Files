import pandas as pd
import matplotlib.pyplot as plt

# load rankings data here:
gt_wood = pd.read_csv('Golden_Ticket_Award_Winners_Wood.csv')
gt_steel = pd.read_csv('Golden_Ticket_Award_Winners_Steel.csv')

# write function to plot rankings over time for 1 roller coaster here:
el_toro = gt_wood[(gt_wood['Name'] == 'El Toro') * (gt_wood['Park'] == 'Six Flags Great Adventure')]
el_toro_years = el_toro['Year of Rank'].values
el_toro_ranks = el_toro.Rank.values

plt.figure(1)
ax = plt.subplot()
plt.plot(el_toro_years, el_toro_ranks, marker = 'o', color = 'blue')
ax.set_yticks([1, 2, 3])
plt.title('El Toro Ranking by Year')
plt.xlabel('Year')
plt.ylabel('Wood Coaster Ranking')
#plt.show()   
plt.close()

# write function to plot rankings over time for 2 roller coasters here:
boulder_dash = gt_wood[(gt_wood['Name'] == 'Boulder Dash')]
boulder_dash_years = boulder_dash['Year of Rank'].values
boulder_dash_ranks = boulder_dash['Rank'].values

plt.figure(2)
ax = plt.subplot()
plt.plot(boulder_dash_years, boulder_dash_ranks, marker = 'o', color = 'red')
plt.plot(el_toro_years, el_toro_ranks, marker = 'o', color = 'blue')
plt.title('El Toro vs Boulder Dash')
#plt.show()   
plt.close()

# write function to plot top n rankings over time here:
def topranking(n,type):
    if type == 'wood':
        top_n_rankings = gt_wood[gt_wood['Rank'] <= n]
    elif type == 'steel':
        top_n_rankings = gt_steel[gt_steel['Rank'] <= n]
    else:
        print('Error: function takes two arguments, n and type.')
    ax2 = plt.subplot()
    for coaster in set(top_n_rankings['Name']):
        coaster_rank_data = top_n_rankings[top_n_rankings['Name'] == coaster]
        plt.plot(coaster_rank_data['Year of Rank'], coaster_rank_data['Rank'], label = coaster, marker = 'o')
    plt.legend()
    plt.title('Top {} coasters'.format(type))
    plt.xlabel('Year')
    plt.ylabel('Rank')
    ax2.set_yticks = range(1,n+1,1)
    plt.show()    
    
#topranking(5,'wood')
plt.close()

# load roller coaster data here:
roller_coasters = pd.read_csv('roller_coasters.csv')
print(roller_coasters.head(), roller_coasters.dtypes)

# write function to plot histogram of column values here:
def make_hist(df, column_name):
    x_values = df[column_name].values
    plt.hist(x_values, color = 'purple', edgecolor = 'black')
    plt.title('Roller Coaster {}'.format(column_name).title())
    plt.xlabel(column_name.title())
    plt.ylabel('Frequency')
    plt.show()

#make_hist(roller_coasters, 'speed')
plt.close()

# write function to plot inversions by coaster at a park here:
def inversions(df, park_name):
    park_df = df[df['park'] == park_name]
    x_val = park_df['name'].values
    y_val = park_df['num_inversions'].values
    ax3 = plt.subplot()
    plt.bar(x_val, y_val)
    plt.title('Number of Inversions at {} by Coaster'.format(park_name.title()))
    plt.xlabel('Coaster Names')
    ax3.set_xticklabels(x_val, rotation = 90)
    plt.ylabel('Number of Inversions')
    plt.tight_layout()
    plt.show()

#inversions(roller_coasters, 'Six Flags Great Adventure')

plt.close()

# write function to plot pie chart of operating status here:
def operation(df):
    num_operating = len(df[df['status'] == 'status.operating'])
    num_closed = len(df[df['status'] == 'status.closed.definitely'])
    plt.pie([num_operating, num_closed], autopct='%d%%', labels = ['operational', 'closed'], colors = ['green', 'red'])
    plt.axis('equal')
    plt.title('Percentage of Operational coasters')
    plt.show()

#operation(roller_coasters)

plt.close()