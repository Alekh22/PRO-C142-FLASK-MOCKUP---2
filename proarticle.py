from flask import Flask,jsonify,request
import csv
allmovies=[]
with open ("article.csv",encoding="utf8")as f:
    reader= csv.reader(f)
    data=list(reader)
    allmovies=data[1:]
liked_article=[]
unliked_article=[]

pp=Flask(__name__)

@app.route("/get-article")
def getarticle():
    return jsonify({"data":article[0],"status":"success"})

@app.route("/liked_article",methods=["POST"])
def likedmovie():
    movies=allmovies[0]
    allmovies=allmovies[1:]
    liked_article.append(movies)
    return jsonify ({"status":"success"}),201

@app.route("/unliked_article",methods=["POST"])
def unlikedmovie():
    movies=allmovies[0]
    allmovies=allmovies[1:]
    unliked_article.append(movies)
    return jsonify ({"status":"success"}),201

if __name__ =="__main__":
    app.run()

    @app.route("/recomendedmovies")
def recomendedmovies():
    all_recomended=[]
    for article in liked_article:
        output=get_recommendations(article[19])
        for data in output:
            all_recomended.append(data)
    import itertools
    all_recomended.sort()
    all_recomended=list(all_recomended for all_recomended,_ in itertools.groupby(all_recomended))
    moviedata=[]
    for article in all_recomended:
        data={"title":article[0],
        "poster_link":article[1],
        "release_date":article[2] or "n/a" ,
        "runtime":article[3],
        "rating":article[4],
        "over_view":article[5]}
       article-data.append(data)
    return jsonify({"data":article-data,"status":"success"}),200



if __name__ == "__main__":
  app.run()
