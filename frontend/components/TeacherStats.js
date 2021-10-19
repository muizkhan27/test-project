import styles from "../styles/TeacherStats.module.css";

export default function TeacherStats({ info }) {
  const chunkSize = 12;
  const singleTeacherStats = info
    .map((e, i) => {
      return i % chunkSize === 0 ? info.slice(i, i + chunkSize) : null;
    })
    .filter((e) => {
      return e;
    });

  return (
    <div>
      <table className={`${styles.stats} table`}>
        <caption className={styles.caption}>
          <h4>Month-Wise Teacher Info</h4>
        </caption>
        <thead>
          <tr>
            <th scope="col">Teacher Name</th>
            <th scope="col">Jan</th>
            <th scope="col">Feb</th>
            <th scope="col">Mar</th>
            <th scope="col">Apr</th>
            <th scope="col">May</th>
            <th scope="col">Jun</th>
            <th scope="col">Jul</th>
            <th scope="col">Aug</th>
            <th scope="col">Sep</th>
            <th scope="col">Oct</th>
            <th scope="col">Nov</th>
            <th scope="col">Dec</th>
          </tr>
        </thead>
        <tbody>
          {singleTeacherStats.map((singleTeacherStat, index) => {
            return (
              <tr key={singleTeacherStat[index].teacher__id}>
                <td>{singleTeacherStat[index].teacher__name}</td>
                {singleTeacherStat.map((monthwise) => {
                  return (
                    <td>{`${Math.floor(monthwise.duration__sum / 60)}H ${
                      monthwise.duration__sum % 60
                    }M`}</td>
                  );
                })}
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
}
