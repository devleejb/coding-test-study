#include <stdio.h>
#include <queue>
#include <vector>
#include <utility>

#define INF 123456789

using namespace std;

int N, M, C, maxVal, cnt;
int d[30001], isVisited[30001];
vector<pair<int, int> > edges[30001];

void dijkstra(int start) {
    int nowVer, nowDis, toVertex, toVertexDis;
    priority_queue<pair<int, int> > pq;

    for (int i = 1; i <= N; ++i) {
        d[i] = INF;
    }

    d[start] = 0;
    isVisited[start] = 1;

    pq.push(make_pair(0, start));

    while (!pq.empty()) {
        nowVer = pq.top().second;
        nowDis = -pq.top().first;

        pq.pop();

        if (nowDis > d[nowVer]) continue;

        for (int i = 0; i < edges[nowVer].size(); ++i) {
            toVertex = edges[nowVer][i].first;
            toVertexDis = nowDis + edges[nowVer][i].second;

            if (isVisited[toVertex] == 0 && d[toVertex] > toVertexDis) {
                d[toVertex] = toVertexDis;

                pq.push(make_pair(-toVertexDis, toVertex));

                if (toVertexDis > maxVal) maxVal = toVertexDis;
            }
        }
    }
     
} 

int main() {
    int X, Y, Z;

    scanf("%d %d %d", &N, &M, &C);

    for (int i = 0; i < M; ++i) {
        scanf("%d %d %d", &X, &Y, &Z);

        edges[X].push_back(make_pair(Y, Z));
    }

    dijkstra(C);

    for (int i = 1; i <= N; ++i) {
        if (d[i] != INF && d[i] != 0) ++cnt;
    }

    printf("%d %d", cnt, maxVal);

    return 0;
}

