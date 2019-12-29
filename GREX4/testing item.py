###test

df_i2 = df_i[df_i.From.str.contains('klay')]
df_i2
df_i3 = df_i2.groupby('From').MessageID.nunique()
df_i3

df_3 = df_i.groupby('From').MessageID.nunique()
df_3