# bibliotecas para visualização dos dados
import matplotlib.pyplot as plt


# funcao para mostrar gols
def show_goals(df):
    """
    Mostra o desempenho do time em gols feitos e tomados pelas temporadas
    fase = regular, playoffs ou tudo
    tipo = soma de todos os gols ou media por temporada
    """
    # lista com o nome dos times
    team_list = list(df["team_name"].sort_values().unique())
    
    fase = input("Digite a fase que quer ver (r, p ou tudo): ")
    tipo = input("Quer ver a soma total ou a media dos gols (total ou media): ")
    
    if (fase == "tudo") & (tipo == "total"):
        for team in list(df["team_name"].sort_values().unique()):
            goals_distrib = df[(df['team_name']== team)].groupby(['season'])[['goals_for','goals_against']].sum()
            goals_distrib = goals_distrib[["goals_for","goals_against"]].rename(columns={"goals_for":"gols feitos",
                                                                                        "goals_against":"gols sofridos"})
            
            show_goals_result(df=df, team=team, tipo=tipo, fase=fase, df2=goals_distrib)
    
    if (fase == "r") & (tipo == "total"):
        for team in list(df["team_name"].sort_values().unique()):
            goals_distrib = df[(df['team_name']== team) & (df["type"]=='R')].groupby(['season'])[['goals_for','goals_against']].sum()
            goals_distrib = goals_distrib[["goals_for","goals_against"]].rename(columns={"goals_for":"gols feitos",
                                                                                        "goals_against":"gols sofridos"})
            
            show_goals_result(df=df, team=team, tipo=tipo, fase=fase, df2=goals_distrib)
            
    if (fase == "p") & (tipo == "total"):
        for team in list(df["team_name"].sort_values().unique()):
            goals_distrib = df[(df['team_name']== team) & (df["type"]=="P")].groupby(['season'])[['goals_for','goals_against']].sum()
            goals_distrib = goals_distrib[["goals_for","goals_against"]].rename(columns={"goals_for":"gols feitos",
                                                                                        "goals_against":"gols sofridos"})
            
            show_goals_result(df=df, team=team, tipo=tipo, fase=fase, df2=goals_distrib)
            
    if (fase == "tudo") & (tipo == "media"):
        for team in list(df["team_name"].sort_values().unique()):
            
            goals_distrib = df[(df['team_name']== team)].groupby(['season'])[['goals_for','goals_against']].mean()
            goals_distrib = goals_distrib[["goals_for","goals_against"]].rename(columns={"goals_for":"media gols feitos",
                                                                                        "goals_against":"media gols sofridos"})
            
            show_goals_result(df=df, team=team, tipo=tipo, fase=fase, df2=goals_distrib)
    
    if (fase == "r") & (tipo == "media"):
        for team in list(df["team_name"].sort_values().unique()):
            goals_distrib = df[(df['team_name']== team) & (df["type"]=='R')].groupby(['season'])[['goals_for','goals_against']].mean()
            goals_distrib = goals_distrib[["goals_for","goals_against"]].rename(columns={"goals_for":"media gols feitos",
                                                                                        "goals_against":"media gols sofridos"})
            
            show_goals_result(df=df, team=team, tipo=tipo, fase=fase, df2=goals_distrib)
            
    if (fase == "p") & (tipo == "media"):
        for team in list(df["team_name"].sort_values().unique()):
            goals_distrib = df[(df['team_name']== team) & (df["type"]=="P")].groupby(['season'])[['goals_for','goals_against']].mean()
            goals_distrib = goals_distrib[["goals_for","goals_against"]].rename(columns={"goals_for":"media gols feitos",
                                                                                        "goals_against":"media gols sofridos"})
            
            show_goals_result(df=df, team=team, tipo=tipo, fase=fase, df2=goals_distrib)
        
    
def show_goals_result(df, team, tipo, fase, df2):
    """
    Plota o resultado escolhido
    """
    goals_mean = df.groupby(["season"])["goals_for"].mean()
    goals_mean_playoffs = df[df["type"]== "P"].groupby(["season"])["goals_for"].mean()
    
    if ((fase == "r") | (fase == "tudo")) & (tipo == "total"):
        fig, ax = plt.subplots(figsize=(8, 4))
    
        df2.plot(color=['steelblue','lightsteelblue'], linewidth=3, ls='-',marker='o', ax=ax)
        ax.set_title(team + ": gols feitos e sofridos por temporada", loc="left", weight="bold", fontsize=16, alpha=0.5, pad=25)
    
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_ylim(0, 400)
        ax.set_xlim(20092010, 20192020)
    
        plt.tight_layout()
    
    if (fase == "p")& (tipo== "total"):
        fig, ax = plt.subplots(figsize=(8, 4))
    
        df2.plot(color=['steelblue','lightsteelblue'], linewidth=3, ls='-',marker='o', ax=ax)
        ax.set_title(team + ": gols feitos e sofridos nos playoffs por temporada", loc="left", weight="bold", fontsize=16, alpha=0.5, pad=25)
    
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_ylim(0, 100)
        ax.set_xlim(20092010, 20192020)
    
        plt.tight_layout()
        
        
    if ((fase == "r") | (fase == "tudo")) & (tipo == "media"):
        
        fig, ax = plt.subplots(figsize=(8, 4))
    
        df2.plot(color=['steelblue','lightsteelblue'], linewidth=3, ls='-',marker='o', ax=ax)
        goals_mean.plot(color="silver", linewidth=3, ls='-',marker='o', label="media gols NHL", ax=ax)
        
        ax.set_title(team + ": media gols feitos e sofridos por temporada", loc="left", weight="bold", fontsize=16, alpha=0.5, pad=25)
    
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_ylim(0, 5)
        ax.set_xlim(20092010, 20192020)
    
        plt.tight_layout()
    
    if (fase == "p") & (tipo== "media"):
        fig, ax = plt.subplots(figsize=(8, 4))
    
        df2.plot(color=['steelblue','lightsteelblue'], linewidth=3, ls='-',marker='o', ax=ax)
        goals_mean_playoffs.plot(color="silver", linewidth=3, ls='-',marker='o', label="media gols NHL", ax=ax)
        
        ax.set_title(team + ": media de gols feitos e sofridos nos playoffs por temporada", loc="left", weight="bold", fontsize=16, alpha=0.5, pad=25)
    
        plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_ylim(0, 5)
        ax.set_xlim(20092010, 20192020)
    
        plt.tight_layout()