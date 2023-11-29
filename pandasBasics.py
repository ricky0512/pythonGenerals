def concat_ordered_columns(frames):
    columns_ordered = []
    for frame in frames:
        columns_ordered.extend(x for x in frame.columns if x not in columns_ordered)
    final_df = pd.concat(frames)    
    return final_df[columns_ordered] 

dfs = [df_a,df_b,df_c]
full_df = concat_ordered_columns(dfs)
